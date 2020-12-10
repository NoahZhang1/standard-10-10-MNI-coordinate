import bpy
import bmesh



MNI_coordinate = {'Fp1':(-21.5,70.2,-0.1),'Fp2':(28.4,69.1,-0.4),'Fz':(0.6,40.9,53.9),'F3':(-35.5,49.4,32,4),'F4':(40.2,47.6,32,1),'F7':(-54.8,33.9,-3.5),'F8':(56.6,30.8,-4.1),'Cz':(0.8,-14.7,73.9),'C3':(-52.2,-16.4,57.8),'C4':(54.1,-18.0,57.5),'T3':(-70.2,-21.3,-10.7),'T4':(71.9,-25.2,-8.2),'Pz':(0.2,-62.1,64.5),'P3':(-39.5,-76.3,47.4),'P4':(36.8,-74.9,49.2),'T5':(-61.5,-65.3,1.1),'T6':(59.3,-67.6,3.8),'O1':(-26.8,-100.2,12.8),'O2':(24.1,-100.5,14.1)}
##10-10 MNI coordinate
Talairach_coordinate = {'Fp1':(-21.3,68,-3.0),'Fp2':(28.1,66.9,-3.6),'Fz':(0.6,42.1,47.5),'F3':(-35.1,49.3,27.4),'F4':(39.8,47.6,27.2),'F7':(-54.2,32.7,-4.4),'F8':(56,29.7,-4.7),'Cz':(0.8,-10.8,68.6),'C3':(-51.7,-13.2,53.9),'C4':(53.6,-14.8,53.7),'T3':(-69.5,-21.1,-8.1),'T4':(71.2,-24.7,-5.8),'Pz':(0.2,-57.2,62.3),'P3':(-39.1,-71.7,47.3),'P4':(36.5,-70.3,48.8),'T5':(-60.9,-63.2,3.9),'T6':(58.7,-65.4,6.4),'O1':(-26.6,-96.5,16.1),'O2':(23.9,-96.7,17.3)}
##10-10 Talairach coordinate

bpy.ops.object.empty_add(type='SPHERE', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) 
##add a origin at 0,0,0

def exectute(positional_dic,radius,depth):
    for i in positional_dic:
        a = positional_dic[i][0]
        b = positional_dic[i][1]
        c = positional_dic[i][2]
        bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, enter_editmode=False, align='WORLD', location=(a, b, c), scale=(1, 1, 1))
        bpy.context.object.name = i
        bpy.ops.object.constraint_add(type='TRACK_TO')
        bpy.context.object.constraints["Track To"].target = bpy.data.objects["Empty"]

       
exectute(Talairach_coordinate,2,5) 
##takes radius and depth as parameter
