import bpy
context = bpy.context
scene = context.scene
# all meshes on mesh objects in scene
meshes = [o.data for o in scene.objects
        if o.type == 'MESH']
# add a new "LightmapUV" UV to each        
for m in meshes:
    if m.uv_layers.get("LightmapUV") is None:
        lightmapuv = m.uv_layers.new(name="LightmapUV")
        lightmapuv.active_render = True
        m.uv_layers.active_index = len(m.uv_layers) - 1
    
# add a new image called LightmapBaked
image = bpy.data.images.get("LightmapBaked")
if image is None:
    image = bpy.data.images.new("LightmapBaked", width=4096, height=4096)

# add an image texture node to each material
for m in bpy.data.materials:
    nodes = m.node_tree.nodes
    
    existing_image_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
    lm_existing = False
    for image_node in existing_image_nodes:
        if image_node.image.name == "LightmapBaked":
            lm_existing = True
            nodes.active = image_node
            break
    if lm_existing:
        print("existing image node with LightmapBaked!")
        continue
    
    principled = next(n for n in nodes if n.type == 'BSDF_PRINCIPLED')
    if principled is None:
        continue
    
    base_color = principled.inputs['Base Color'] #Or principled.inputs[0]
    
    teximage = nodes.new("ShaderNodeTexImage")
    teximage.image = image
    nodes.active = teximage
    m.node_tree.links.new(base_color, teximage.outputs['Color'])
    