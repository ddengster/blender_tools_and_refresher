import bpy

# add an image texture node to each material
for m in bpy.data.materials:
    #print("-- " + m.name)
    nodes = m.node_tree.nodes
    
    image_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
    lm_existing = False
    lmbaked = None
    unlinked_node = None
    for image_node in image_nodes:
        #print(image_node.image.name)
        #print(type(image_node))
        if image_node.outputs[0].is_linked == False:
            unlinked_node = image_node
        if image_node.image.name == "LightmapBaked":
            lmbaked = image_node
            
    if lmbaked is None:
        continue
        
    principled = next(n for n in nodes if n.type == 'BSDF_PRINCIPLED')
    if principled is None:
        continue
    
    base_color = principled.inputs['Base Color'] #Or principled.inputs[0]
    if base_color is None:
        continue

    if unlinked_node is not None:
        m.node_tree.links.new(base_color, unlinked_node.outputs['Color'])

# all meshes on mesh objects in scene
context = bpy.context
scene = context.scene

meshes = [o.data for o in scene.objects
        if o.type == 'MESH']
for m in meshes:
    if m.uv_layers.get("LightmapUV") is None:
        continue
    #m.uv_layers[0].active_render = not m.uv_layers[0].active_render
    #m.uv_layers.get("LightmapUV").active_render = not m.uv_layers.get("LightmapUV").active_render
    
    std_uv = m.uv_layers[0]
    lightmapuv = m.uv_layers.get("LightmapUV")
    
    print("std_uv: " + std_uv.name)
    print("lightmapuv: " + lightmapuv.name)
    
    print(std_uv.active_render)
    print(lightmapuv.active_render)
    
    if m.uv_layers.active_index is 0:
        m.uv_layers.active_index = 1
        lightmapuv.active_render = True
    else:
        m.uv_layers.active_index = 0
        std_uv.active_render = True
