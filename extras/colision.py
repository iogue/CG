"""Textures examples"""

from turtle import distance
import numpy as np
import math
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig
from extras.movement_rig_obj import MovementRigObject
from core_ext.texture import Texture
from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial
from geometry.arrow import ArrowMesh #Diogo Bastista
from geometry.target import TargetMesh #Carlos Carvalho
from geometry.tripe import TripeMesh
from geometry.bow import BowMesh
from geometry.prisma import PrismaMesh
from geometry.target_hitbox import TargetHitMesh
import pygame



class Example(Base):
    """ Render a textured square """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        
        self.camera.set_position([-1.5, 0, 10])
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 0,0])
        self.scene.add(self.rig)  
        self.mesh_hitbox = PrismaMesh()
        self.mesh_tripe = TripeMesh()
        self.mesh_arrow = ArrowMesh()
        self.mesh_hittarget= TargetHitMesh()
        self.mesh_target = TargetMesh()
        
        
        self.rig_arrow = MovementRigObject()
        
        self.rig_arrow.add(self.mesh_arrow)  
        #self.rig_arrow.add(self.mesh_hitbox) 
        
        self.scene.add(self.mesh_target)
        #self.scene.add(self.mesh_hittarget)
        self.scene.add(self.rig_arrow)

       
        
        
        #self.mesh_target.rotate_x(math.pi/2)
        
        self.mesh_target.translate(1,1,-1)
        self.mesh_arrow.translate(0,-2,0)
        self.mesh_arrow.scale(1)
        self.rig_arrow.set_position([0,0,0])
        self.rig_arrow.translate(1,1,1)
        
        
       

    def update(self):
        self.rig.update(self.input, self.delta_time*2)
        self.rig_arrow.update(self.input, self.delta_time*2)


        # minArrowX= self.mesh_arrow.global_position[0] 
        # minArrowY= self.mesh_arrow.global_position[1] 
        # minArrowZ= self.mesh_arrow.global_position[2] 
        arrowX= self.mesh_arrow.global_position[0] 
        arrowY= self.mesh_arrow.global_position[1]  
        arrowZ= self.mesh_arrow.global_position[2] 
        
        targetCenterX=self.mesh_target.global_position[0]
        targetCenterY=self.mesh_target.global_position[1]
        targetCenterZ=self.mesh_target.global_position[2]
        
        list1= [targetCenterX,targetCenterY,targetCenterZ]
        list2= [arrowX,arrowY,arrowZ]
        vector1=np.array(list1)
        vector2=np.array(list2)
       

        
        raioCircunferencia=0.8
        
        
        dist1= math.sqrt(abs( (vector2[0]-vector1[0])*(vector2[0]-vector1[1])+(vector2[1]-vector1[1])*(vector2[1]-vector1[1]) +(vector2[2]-vector1[2])*(vector2[2]-vector1[2])-raioCircunferencia*raioCircunferencia))

        yMax = 2
        yMin = 0.052
        zPlane = 2.9


        if ( dist1 <= 1.93  and zPlane >= arrowZ and yMin<arrowY<yMax):
            print('hit')
            print(vector1)
            print(vector2)
            print('...........................')
        else:
            print(vector2)
            print(dist1)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
