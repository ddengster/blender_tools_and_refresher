
# (Unity) FBX with animations to blender

- Assumes that FBX animations are seperated, and there is one skinned model without animations. Animations have the format `Model Name`@`Animation Name`.FBX

- Import the FBX with only the mesh and armature. 

- Import the FBX that has your desired animation. (usually this is `Model Name`@`Animation Name`.FBX). Note that the new nodes/armature/mesh will be postfixed with '.00X'

- Select and delete all **.00X** nodes/armature/mesh that were imported.

- Setup your UI. Right click, select **Horizontal Split** and change it to **Dope Sheet**. Then switch the dropdown next to it from **Dope Sheet** to **Action Editor**. You should have 3 panels

![](hsplit.PNG)

![](ds.PNG)

![](actioneditor.PNG)

- Switch your **Timeline Editor** to **Nonlinear Animation**

![](nla.PNG)

## Migrating animations

- Goto the **Action Editor**. You will see many actions with the format 'ObjectName|Take|Layer'. Our job is to integrate them with the original mesh and any additional nodes

![](listofactions.PNG)

1. Select your original **Armature** within **Scene Collection**, the top right box. Then select the action 'Armature.001|Take|Layer' similar to above picture and scrub the timeline. The model should play the animation.

2. Rename 'Armature.001|Take|Layer' to **animationName**. 

3. Hit 'Push down' button. Note **NlaTrack** has been created (in red). Rename it to Idle. Then delete the mesh, and the parent armature (postfixed with .001) .

![](rename.PNG)

- Repeat the steps 1 to 3 for each scene collection item and animation pair (eg. Rig node with Rig.001|Take.001|BaseLayer, RigLArmGizmo with RigLArmGizmo.001|Take.001|BaseLayer, etc), but with **_<animationname>** for the renaming in the action editor.

- The renaming of Nla animation tracks can be done all at once before importing another animation

- Repeat for all other animations

### Viewing animations

- Make sure the current action in the **Action Editor** is nothing (undo if so; blender seems to treat changes there as modifications to the data), **select nothing** in the scene.

- In the NLA panel left click on your desired action, then right click on it and do **Track Ordering -> To Top**.

- Scrub the timeline to see the animation.

![nla_ordering](https://github.com/user-attachments/assets/aef54178-60f7-4269-bbbd-20b66e845601)


## Material names and textures

- Select your mesh, rename it's material to "SkinnedUnit"

![](materialname.PNG)

- Also change Base color to image texture, and pick your texture (for engine consumption purposes, follow the docs to name it (eg. <..>_a.png, <..>_b.png))

![](imagetexture.PNG)

- Select viewport shading to view/spotcheck the texture in the scene 

![](view_texture.PNG)
