import random
import numpy as np
import math
import pathlib
import sys

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig
from core_ext.texture import Texture
from geometry.cylinder import CylinderGeometry
from geometry.handle import HandleGeometry
from geometry.sphere import SphereGeometry
from material.texture import TextureMaterial
from geometry.bow import BowMesh
from extras.movement_player import MovementPlayer
from geometry.arrow import ArrowMesh
from geometry.target import TargetMesh
from geometry.tripe import TripeMesh
from extras.movement_arrow import MovementArrow
from geometry.rectangle import RectangleGeometry
from material.sprite import SpriteMaterial
from geometry.game_over import GameOver
from geometry.main_page import MainPageMesh
from geometry.instructions import InstructionsMesh
from geometry.winning import Winning
from extras.movement_camera import MovementCamera
from core.matrix import Matrix
from geometry.scenario import ScenarioMesh

class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.cameraRig = MovementCamera()
        self.rig = MovementRig()
        self.cameraRig.add(self.camera)
        self.rig.add(self.cameraRig)
        # self.camera.set_position([0,0,5])
        self.bow = BowMesh()
        self.bow.scale(0.5)
        self.arrow = ArrowMesh()
        self.bow.set_position([-0.3,0,-0.3])
        self.arrow.set_position([-0.175,0.3,0])
        self.arrow.rotate_x(-math.pi/2, local=False)


        geometry = RectangleGeometry(width = 0.5, height = 0.125)
        tile_set = Texture("images/energy_bar.png")
        sprite_material = SpriteMaterial(tile_set, {
            "billboard" : 1, 
            "tileCount" : [1, 4],
            "tileNumber" : 0 
        })

        geometry1 = RectangleGeometry(width = 0.5, height = 0.125)
        tile_set1 = Texture("images/arrow_number1.png")
        sprite_material1 = SpriteMaterial(tile_set1, {
            "billboard" : 1, 
            "tileCount" : [1, 4],
            "tileNumber" : 0 
        })

        geometry2 = RectangleGeometry(width = 0.5, height = 0.1)
        tile_set2 = Texture("images/niveis.png")
        sprite_material2 = SpriteMaterial(tile_set2, {
            "billboard" : 1, 
            "tileCount" : [1, 5],
            "tileNumber" : 0 
        })

        geometry3 = RectangleGeometry(width = 0.15, height = 0.2)
        tile_set3 = Texture("images/wind_colors.png")
        sprite_material3 = SpriteMaterial(tile_set3, {
            "billboard" : 1, 
            "tileCount" : [3, 2],
            "tileNumber" : 0 
        })

        self.mainPage = MainPageMesh()
        self.mainPage.set_position([10, 0, -100])
        
        # self.scenario = ScenarioMesh()
        # self.scenario.set_position([0, 0, 0])

        self.instructions = InstructionsMesh()
        self.instructions.set_position([7.5, 0, -100])

        self.gameOver = GameOver()
        self.gameOver.set_position([5, 0, -100])

        self.winning = Winning()
        self.winning.set_position([2.5, 0, -100])

        self.sprite = Mesh(geometry, sprite_material)
        self.sprite.set_position([0.55,-0.45,-1])
        self.sprite1 = Mesh(geometry1, sprite_material1)
        self.sprite1.set_position([0.55,-0.3,-1])
        self.sprite2 = Mesh(geometry2, sprite_material2)
        self.sprite2.set_position([0,0.55,-1])
        self.sprite3 = Mesh(geometry3, sprite_material3)
        self.sprite3.set_position([0,0.45,-1])
        self.rig.add(self.bow)
        self.rig.add(self.arrow)
        self.rig.add(self.sprite)
        self.rig.add(self.sprite1)
        self.rig.add(self.sprite2)
        self.rig.add(self.sprite3)
        self.rig.set_position([0, 0, 20])
        self.scene.add(self.rig)

        self.arrows=[]
        self.arrows.append(ArrowMesh())
        self.arrows.append(ArrowMesh())
        self.arrows.append(ArrowMesh())
        self.arrows[0].set_position([-2, 0, 100])
        self.arrows[1].set_position([-2, 2, 100])
        self.arrows[2].set_position([2, 0, 100])

        self.target = TargetMesh()
        self.target.rotate_x(math.pi/2)
        self.target.translate(-0.1,0.3,0.4) #x->translacao , y->altitude , z->profundidade

        self.tripe = TripeMesh()
        self.tripe.translate(-0.75,-0.9,0)

        # LEVEL 1
        self.sky_geometry = SphereGeometry(radius=50)
        self.sky_material = TextureMaterial(texture=Texture(file_name="images/sky1.jpg"), property_dict={"doubleSide": True})
        self.sky = Mesh(self.sky_geometry, self.sky_material)
        self.scene.add(self.sky)
        self.grass_geometry = RectangleGeometry(width=100, height=100)
        self.grass_material = TextureMaterial(
            texture=Texture(file_name="images/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        self.grass = Mesh(self.grass_geometry, self.grass_material)
        self.grass.rotate_x(-math.pi/2)
        self.grass.translate(0,0,-1.5)
        self.scene.add(self.grass)
        #=================================================

        # LEVEL 2
        self.sky_geometry1 = SphereGeometry(radius=50)
        self.sky_material1 = TextureMaterial(texture=Texture(file_name="images/sky1.jpg"), property_dict={"doubleSide": True})
        self.sky1 = Mesh(self.sky_geometry1, self.sky_material1)
        self.sky1.translate(101,0,0)
        self.scene.add(self.sky1)
        self.grass_geometry1 = RectangleGeometry(width=100, height=100)
        self.grass_material1 = TextureMaterial(
            texture=Texture(file_name="images/sand.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        self.grass1 = Mesh(self.grass_geometry1, self.grass_material1)
        self.grass1.rotate_x(-math.pi/2)
        self.grass1.translate(101,0,-3)
        self.scene.add(self.grass1)
        #=================================================

        # LEVEL 3
        self.sky_geometry2 = SphereGeometry(radius=50)
        self.sky_material2 = TextureMaterial(texture=Texture(file_name="images/night.jpg"), property_dict={"doubleSide": True})
        self.sky2 = Mesh(self.sky_geometry2, self.sky_material2)
        self.sky2.translate(-101,0,0)
        self.scene.add(self.sky2)
        self.grass_geometry2 = RectangleGeometry(width=100, height=100)
        self.grass_material2 = TextureMaterial(
            texture=Texture(file_name="images/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        self.grass2 = Mesh(self.grass_geometry2, self.grass_material2)
        self.grass2.rotate_x(-math.pi/2)
        self.grass2.translate(-101,0,-3)
        self.scene.add(self.grass2)
        #=================================================

        # LEVEL 4
        nether_sky_geometry = SphereGeometry(radius=50)
        nether_sky_material = TextureMaterial(texture=Texture(file_name="images/red_sky.jpg"), property_dict={"doubleSide": True})
        nether_sky = Mesh(nether_sky_geometry, nether_sky_material)
        nether_sky.translate(202,0,0)
        self.scene.add(nether_sky)
        nether_geometry = RectangleGeometry(width=100, height=100)
        nether_material = TextureMaterial(
            texture=Texture(file_name="images/nether.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        nether = Mesh(nether_geometry, nether_material)
        nether.rotate_x(-math.pi/2)
        nether.translate(202,0,-3)
        self.scene.add(nether) 
        #=================================================

        # LEVEL 5
        end_sky_geometry = SphereGeometry(radius=50)
        end_sky_material = TextureMaterial(texture=Texture(file_name="images/end_sky.jpg"), property_dict={"doubleSide": True})
        end_sky = Mesh(end_sky_geometry, end_sky_material)
        end_sky.translate(-202,0,0)
        self.scene.add(end_sky)
        end_geometry = RectangleGeometry(width=100, height=100)
        end_material = TextureMaterial(
            texture=Texture(file_name="images/end.jpg"),
            property_dict={"repeatUV": [40, 40]}
        )
        end = Mesh(end_geometry, end_material)
        end.rotate_x(-math.pi/2)
        end.translate(-202,0,-3)
        self.scene.add(end)
        #=================================================

        # SCENARIO LEVEL 1
        tree_material = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry = RectangleGeometry(10,10)
        tree_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree = Mesh(tree_geometry, tree_material)
        self.tree.set_position([10, 3.12, 0])
        self.scene.add(self.tree)

        tree_material1 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry1 = RectangleGeometry(10,10)
        tree_geometry1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree1 = Mesh(tree_geometry1, tree_material1)
        self.tree1.set_position([15, 3.12, 10])
        self.scene.add(self.tree1)

        tree_material2 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry2 = RectangleGeometry(10,10)
        tree_geometry2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree2 = Mesh(tree_geometry2, tree_material2)
        self.tree2.set_position([-10, 3.12, 0])
        self.scene.add(self.tree2)

        tree_material3 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry3 = RectangleGeometry(10,10)
        tree_geometry3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree3 = Mesh(tree_geometry3, tree_material3)
        self.tree3.set_position([-15, 3.12, 10])
        self.scene.add(self.tree3)

        tree_material4 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry4 = RectangleGeometry(10,10)
        tree_geometry4.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree4 = Mesh(tree_geometry4, tree_material4)
        self.tree4.set_position([-15, 3.12, 20])
        self.scene.add(self.tree4)

        tree_material5 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry5 = RectangleGeometry(10,10)
        tree_geometry5.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree5 = Mesh(tree_geometry5, tree_material5)
        self.tree5.set_position([15, 3.12, 20])
        self.scene.add(self.tree5)

        tree_material6 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry6 = RectangleGeometry(10,10)
        tree_geometry6.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree6 = Mesh(tree_geometry6, tree_material6)
        self.tree6.set_position([-10, 3.12, 30])
        self.scene.add(self.tree6)

        tree_material7 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry7 = RectangleGeometry(10,10)
        tree_geometry7.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree7 = Mesh(tree_geometry7, tree_material7)
        self.tree7.set_position([10, 3.12, 30])
        self.scene.add(self.tree7)

        tree_material8 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        tree_geometry8 = RectangleGeometry(10,10)
        tree_geometry8.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree8 = Mesh(tree_geometry8, tree_material8)
        self.tree8.set_position([0, 3.12, 35])
        self.scene.add(self.tree8)

        # tree_material9 = TextureMaterial(texture=Texture(file_name="images/tree.png"))
        # tree_geometry9 = RectangleGeometry(10,10)
        # tree_geometry9.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        # self.tree9 = Mesh(tree_geometry9, tree_material9)
        # self.tree9.set_position([0, 3.12, -10])
        # self.scene.add(self.tree9)

        self.scene.add(self.arrows[0])
        self.scene.add(self.arrows[1])
        self.scene.add(self.arrows[2])
        self.scene.add(self.target)
        self.scene.add(self.tripe)
        self.scene.add(self.mainPage)
        self.scene.add(self.instructions)
        self.scene.add(self.gameOver)
        self.scene.add(self.winning)
        # self.scene.add(self.scenario)

        self.lives = 3
        self.angle = 0
        self.shooting = False
        self.level = 1

        self.tiro = -1
        self.collision = False
        self.win = False
        self.wind = random.randint(1,2)
        self.sprite3.material.uniform_dict["tileNumber"].data = self.wind
        self.moveWind = 0


    def update(self):
        # self.scenario.look_at(self.camera.global_position)
        self.tree.look_at(self.camera.global_position)
        self.tree1.look_at(self.camera.global_position)
        self.tree2.look_at(self.camera.global_position)
        self.tree3.look_at(self.camera.global_position)
        self.tree4.look_at(self.camera.global_position)
        self.tree5.look_at(self.camera.global_position)
        self.tree6.look_at(self.camera.global_position)
        self.tree7.look_at(self.camera.global_position)
        self.tree8.look_at(self.camera.global_position)
        # self.tree9.look_at(self.camera.global_position)

        self.cameraRig.update(self.input, self.level, self.win)
        self.renderer.render(self.scene, self.camera)
        if self.wind == 0:
            self.moveWind = 0.1
        elif self.wind == 1:
            self.moveWind = -0.01
        elif self.wind == 2:
            self.moveWind = 0.01
        elif self.wind == 3:
            self.moveWind = 0.05
        elif self.wind == 4:
            self.moveWind = -0.1
        elif self.wind == 5:
            self.moveWind = -0.05

        self.sprite2.material.uniform_dict["tileNumber"].data = self.level-1
        if self.cameraRig.isGame == True:
            self.rig.update(self.input, self.delta_time*2)
            if self.level == 5:
                self.rig.set_position([0,0,20])
            if self.level == 2:
                self.rig.set_position([100,0,20])
            if self.level == 3:
                self.rig.set_position([-100,0,20])
            if self.level == 4:
                self.rig.set_position([200,0,20])
            if self.level == 5:
                self.rig.set_position([-200,0,20])
            if self.level == 6:
                self.level = 1
                self.wind = random.randint(1,2)
                self.sprite3.material.uniform_dict["tileNumber"].data = self.wind
            if self.lives == 0 and self.collision == True:
                if self.level == 1:
                    self.wind = np.random.choice(np.arange(0, 6), p=[0.1, 0.25, 0.25, 0.15, 0.1, 0.15])
                elif self.level == 2:
                    self.wind = np.random.choice(np.arange(0, 6), p=[0.1, 0.15, 0.15, 0.25, 0.1, 0.25])
                elif self.level == 3:
                    self.wind = np.random.choice(np.arange(0, 6), p=[0.2, 0.10, 0.10, 0.2, 0.2, 0.2])
                elif self.level == 4:
                    self.wind = np.random.choice(np.arange(0, 6), p=[0.3, 0, 0, 0.2, 0.3, 0.2])
                self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())
                self.lives = 3
                self.tiro = -1
                self.level = self.level+1
                self.rig.set_position([0,0,20])
                self.arrows[0].set_position([-2, 0, 100])
                self.arrows[1].set_position([-2, 2, 100])
                self.arrows[2].set_position([2, 0, 100])
                
                self.sprite3.material.uniform_dict["tileNumber"].data = self.wind
            if self.rig.isShooting() == True and self.shooting == False:
                # self.tiro = self.tiro+1
                self.shooting = True
                self.arrows[self.tiro].set_local_matrix(self.arrow.global_matrix)
                self.rig._look_attachment.children_list[2].set_position([-0.175,0,5])
                self.lives = self.lives-1
                self.collision = False
            
            if self.rig.isShooting() == True and self.shooting == True:
                if self.rig.getPower() < 5:
                    self.angle = self.angle + 1/self.rig.getPower()*0.1
                elif self.rig.getPower() < 30:
                    self.angle = self.angle + 1/self.rig.getPower()*0.5
                else:
                    self.angle = self.angle + 1/self.rig.getPower()*1
                self.arrows[self.tiro].translate(self.moveWind,self.rig.getPower()*0.01,math.cos(self.angle)-1)
            else:
                self.shooting = False
                self.angle = 0
                self.rig._look_attachment.children_list[2].set_position([-0.175,0,0])
                tileNumber = math.floor(self.rig.getPower() / 30)
                self.sprite.material.uniform_dict["tileNumber"].data = tileNumber
                tileNumber1 = self.lives
                self.sprite1.material.uniform_dict["tileNumber"].data = tileNumber1
                self.rig.update(self.input, self.delta_time)
        else:
            
            self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())
        


        #COLLISION
        arrowX= self.arrows[self.tiro].global_position[0]
        arrowY= self.arrows[self.tiro].global_position[2]  
        arrowZ= self.arrows[self.tiro].global_position[1]
        
        targetCenterX=self.target.global_position[0]
        targetCenterY=self.target.global_position[1]
        targetCenterZ=self.target.global_position[2]
        
        list1= [targetCenterX,targetCenterY,targetCenterZ]
        list2= [arrowX,arrowY,arrowZ]
        vector1=np.array(list1)
        vector2=np.array(list2)
        
        raioCircunferencia=0.8
        
        
        dist1= math.sqrt(abs((vector2[0]-vector1[0])*(vector2[0]-vector1[1])+(vector2[1]-vector1[1])*(vector2[1]-vector1[1]) +(vector2[2]-vector1[2])*(vector2[2]-vector1[2])-raioCircunferencia*raioCircunferencia))

        yMax = 2
        yMin = 0.052
        zPlane = 2.9


        if ( dist1 <= 0.93  and zPlane >= arrowZ and yMin<arrowY<yMax):
            self.rig.setShooting(False)
            self.collision = True
            if self.tiro < 2:
                self.tiro = self.tiro + 1
                self.rig.setPower(0)

        if self.arrows[self.tiro].global_position[1] < -3+0.175:
            self.rig.setShooting(False)
            self.collision = True
            if self.tiro < 2:
                self.tiro = self.tiro + 1
                self.rig.setPower(0)
        #==============================

        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
