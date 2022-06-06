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
from geometry.pyramid import PyramidGeometry
from material.sprite import SpriteMaterial
from geometry.game_over import GameOver
from geometry.main_page import MainPageMesh
from geometry.instructions import InstructionsMesh
from geometry.winning import Winning
from extras.movement_camera import MovementCamera
from core.matrix import Matrix

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
        self.grass.translate(0,0,-3)
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
        self.tree.set_position([10, 1.65, 0])
        self.scene.add(self.tree)

        tree_geometry1 = RectangleGeometry(10,10)
        tree_geometry1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree1 = Mesh(tree_geometry1, tree_material)
        self.tree1.set_position([15, 1.65, 10])
        self.scene.add(self.tree1)

        tree_geometry2 = RectangleGeometry(10,10)
        tree_geometry2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree2 = Mesh(tree_geometry2, tree_material)
        self.tree2.set_position([-10, 1.65, 0])
        self.scene.add(self.tree2)

        tree_geometry3 = RectangleGeometry(10,10)
        tree_geometry3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree3 = Mesh(tree_geometry3, tree_material)
        self.tree3.set_position([-15, 1.65, 10])
        self.scene.add(self.tree3)

        tree_geometry4 = RectangleGeometry(10,10)
        tree_geometry4.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree4 = Mesh(tree_geometry4, tree_material)
        self.tree4.set_position([-15, 1.65, 20])
        self.scene.add(self.tree4)

        tree_geometry5 = RectangleGeometry(10,10)
        tree_geometry5.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree5 = Mesh(tree_geometry5, tree_material)
        self.tree5.set_position([15, 1.65, 20])
        self.scene.add(self.tree5)

        tree_geometry6 = RectangleGeometry(10,10)
        tree_geometry6.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree6 = Mesh(tree_geometry6, tree_material)
        self.tree6.set_position([-10, 1.65, 35])
        self.scene.add(self.tree6)

        tree_geometry7 = RectangleGeometry(10,10)
        tree_geometry7.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree7 = Mesh(tree_geometry7, tree_material)
        self.tree7.set_position([10, 1.65, 35])
        self.scene.add(self.tree7)

        tree_geometry8 = RectangleGeometry(10,10)
        tree_geometry8.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.tree8 = Mesh(tree_geometry8, tree_material)
        self.tree8.set_position([0, 1.65, 35])
        self.scene.add(self.tree8)

        gate_material = TextureMaterial(texture=Texture(file_name="images/gate.png"))
        gate_geometry = RectangleGeometry(15,10)
        self.gate = Mesh(gate_geometry, gate_material)
        self.gate.set_position([0, -1.5, -30])
        self.scene.add(self.gate)

        gate_material1 = TextureMaterial(texture=Texture(file_name="images/gate2.png"), property_dict={"doubleSide": True})
        gate_geometry1 = RectangleGeometry(15,10)
        self.gate1 = Mesh(gate_geometry1, gate_material1)
        self.gate1.set_position([14.5, -1.5, -30])
        self.scene.add(self.gate1)

        gate_geometry2 = RectangleGeometry(15,10)
        self.gate2 = Mesh(gate_geometry2, gate_material1)
        self.gate2.set_position([29, -1.5, -30])
        self.scene.add(self.gate2)

        gate_geometry3 = RectangleGeometry(15,10)
        self.gate3 = Mesh(gate_geometry3, gate_material1)
        self.gate3.set_position([-14.5, -1.5, -30])
        self.scene.add(self.gate3)

        gate_geometry4 = RectangleGeometry(15,10)
        self.gate4 = Mesh(gate_geometry4, gate_material1)
        self.gate4.set_position([-29, -1.5, -30])
        self.scene.add(self.gate4)

        gate_geometry5 = RectangleGeometry(15,10)
        self.gate5 = Mesh(gate_geometry5, gate_material1)
        self.gate5.set_position([-36.25, -1.5, -22.75])
        self.gate5.rotate_y(math.pi/2)
        self.scene.add(self.gate5)

        gate_geometry6 = RectangleGeometry(15,10)
        self.gate6 = Mesh(gate_geometry6, gate_material1)
        self.gate6.set_position([36.25, -1.5, -22.75])
        self.gate6.rotate_y(math.pi/2)
        self.scene.add(self.gate6)

        gate_geometry7 = RectangleGeometry(15,10)
        self.gate7 = Mesh(gate_geometry7, gate_material1)
        self.gate7.set_position([-36.25, -1.5, -8.25])
        self.gate7.rotate_y(math.pi/2)
        self.scene.add(self.gate7)

        gate_geometry8 = RectangleGeometry(15,10)
        self.gate8 = Mesh(gate_geometry8, gate_material1)
        self.gate8.set_position([36.25, -1.5, -8.25])
        self.gate8.rotate_y(math.pi/2)
        self.scene.add(self.gate8)

        gate_geometry9 = RectangleGeometry(15,10)
        self.gate9 = Mesh(gate_geometry9, gate_material1)
        self.gate9.set_position([-36.25, -1.5, 6.25])
        self.gate9.rotate_y(math.pi/2)
        self.scene.add(self.gate9)

        gate_geometry10 = RectangleGeometry(15,10)
        self.gate10 = Mesh(gate_geometry10, gate_material1)
        self.gate10.set_position([36.25, -1.5, 6.25])
        self.gate10.rotate_y(math.pi/2)
        self.scene.add(self.gate10)

        gate_geometry11 = RectangleGeometry(15,10)
        self.gate11 = Mesh(gate_geometry11, gate_material1)
        self.gate11.set_position([-36.25, -1.5, 20.75])
        self.gate11.rotate_y(math.pi/2)
        self.scene.add(self.gate11)

        gate_geometry12 = RectangleGeometry(15,10)
        self.gate12 = Mesh(gate_geometry12, gate_material1)
        self.gate12.set_position([36.25, -1.5, 20.75])
        self.gate12.rotate_y(math.pi/2)
        self.scene.add(self.gate12)

        gate_geometry13 = RectangleGeometry(15,10)
        self.gate13 = Mesh(gate_geometry13, gate_material1)
        self.gate13.set_position([-29, -1.5, 28])
        self.scene.add(self.gate13)

        gate_geometry14 = RectangleGeometry(15,10)
        self.gate14 = Mesh(gate_geometry14, gate_material1)
        self.gate14.set_position([29, -1.5, 28])
        self.scene.add(self.gate14)

        gate_geometry15 = RectangleGeometry(15,10)
        self.gate15 = Mesh(gate_geometry15, gate_material1)
        self.gate15.set_position([-14.5, -1.5, 28])
        self.scene.add(self.gate15)

        gate_geometry16 = RectangleGeometry(15,10)
        self.gate16 = Mesh(gate_geometry16, gate_material1)
        self.gate16.set_position([14.5, -1.5, 28])
        self.scene.add(self.gate16)

        gate_geometry17 = RectangleGeometry(15,10)
        self.gate17 = Mesh(gate_geometry17, gate_material1)
        self.gate17.set_position([0, -1.5, 28])
        self.scene.add(self.gate17)

        #=================================================

        # SCENARIO LEVEL 2

        big_pyramid_material = TextureMaterial(texture=Texture(file_name="images/pyramid.jpg"), property_dict={"repeatUV": [25, 25]})
        big_pyramid = PyramidGeometry(radius=30, height=30, sides=4, height_segments=25)
        self.big_pyramid = Mesh(big_pyramid, big_pyramid_material)
        self.big_pyramid.set_position([140, 3.12, -25])
        self.scene.add(self.big_pyramid)

        medium_pyramid_material = TextureMaterial(texture=Texture(file_name="images/pyramid.jpg"), property_dict={"repeatUV": [25, 25]})
        medium_pyramid = PyramidGeometry(radius=20, height=20, sides=4, height_segments=25)
        self.medium_pyramid = Mesh(medium_pyramid, medium_pyramid_material)
        self.medium_pyramid.set_position([80, 3.12, -25])
        self.scene.add(self.medium_pyramid)

        small_pyramid_material = TextureMaterial(texture=Texture(file_name="images/pyramid.jpg"), property_dict={"repeatUV": [25, 25]})
        small_pyramid = PyramidGeometry(radius=10, height=10, sides=4, height_segments=25)
        self.small_pyramid = Mesh(small_pyramid, small_pyramid_material)
        self.small_pyramid.set_position([140, 0, 10])
        self.scene.add(self.small_pyramid)

        camel_material = TextureMaterial(texture=Texture(file_name="images/camel.png"))
        camel = RectangleGeometry(5,5)
        self.camel = Mesh(camel, camel_material)
        camel.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.camel.set_position([106, 0, 22.5])
        self.scene.add(self.camel)

        camel1 = RectangleGeometry(2.5,2.5)
        self.camel1 = Mesh(camel1, camel_material)
        camel1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.camel1.set_position([60, -2, 0])
        self.scene.add(self.camel1)

        camel2 = RectangleGeometry(2.5,2.5)
        self.camel2 = Mesh(camel2, camel_material)
        camel2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.camel2.set_position([120, -2, -30])
        self.scene.add(self.camel2)

        camel3 = RectangleGeometry(2.5,2.5)
        self.camel3 = Mesh(camel3, camel_material)
        camel3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.camel3.set_position([60, -2, 5])
        self.scene.add(self.camel3)

        camel4 = RectangleGeometry(2.5,2.5)
        self.camel4 = Mesh(camel4, camel_material)
        camel4.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.camel4.set_position([60, -2, -15])
        self.scene.add(self.camel4)

        palm_material = TextureMaterial(texture=Texture(file_name="images/palm.png"))
        palm = RectangleGeometry(15,15)
        self.palm = Mesh(palm, palm_material)
        palm.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.palm.set_position([60, 0, -25])
        self.scene.add(self.palm)

        palm1 = RectangleGeometry(15,15)
        self.palm1 = Mesh(palm1, palm_material)
        palm1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.palm1.set_position([89, 0, -35])
        self.scene.add(self.palm1)

        palm2 = RectangleGeometry(15,15)
        self.palm2 = Mesh(palm2, palm_material)
        palm2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.palm2.set_position([140, 0, -5])
        self.scene.add(self.palm2)

        palm3 = RectangleGeometry(15,15)
        self.palm3 = Mesh(palm3, palm_material)
        palm3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.palm3.set_position([140, 0, 20])
        self.scene.add(self.palm3)

        #=================================================

        # SCENARIO LEVEL 3
        grave_material = TextureMaterial(texture=Texture(file_name="images/spooky_tree.png"), property_dict={"doubleSide": True})
        grave_geometry = RectangleGeometry(2,3)
        grave_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave = Mesh(grave_geometry, grave_material)
        self.grave.set_position([-91, -1.5, -20])
        self.scene.add(self.grave)

        grave_geometry1 = RectangleGeometry(2,3)
        grave_geometry1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave1 = Mesh(grave_geometry1, grave_material)
        self.grave1.set_position([-91, -1.5, -15])
        self.scene.add(self.grave1)

        grave_geometry2 = RectangleGeometry(2,3)
        grave_geometry2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave2 = Mesh(grave_geometry2, grave_material)
        self.grave2.set_position([-91, -1.5, -10])
        self.scene.add(self.grave2)

        grave_geometry3 = RectangleGeometry(2,3)
        grave_geometry3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave3 = Mesh(grave_geometry3, grave_material)
        self.grave3.set_position([-91, -1.5, -5])
        self.scene.add(self.grave3)

        grave_geometry4 = RectangleGeometry(2,3)
        grave_geometry4.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave4 = Mesh(grave_geometry4, grave_material)
        self.grave4.set_position([-91, -1.5, 0])
        self.scene.add(self.grave4)

        grave_geometry5 = RectangleGeometry(2,3)
        grave_geometry5.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave5 = Mesh(grave_geometry5, grave_material)
        self.grave5.set_position([-91, -1.5, 5])
        self.scene.add(self.grave5)

        grave_geometry6 = RectangleGeometry(2,3)
        grave_geometry6.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave6 = Mesh(grave_geometry6, grave_material)
        self.grave6.set_position([-91, -1.5, 10])
        self.scene.add(self.grave6)

        grave_geometry7 = RectangleGeometry(2,3)
        grave_geometry7.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave7 = Mesh(grave_geometry7, grave_material)
        self.grave7.set_position([-91, -1.5, 15])
        self.scene.add(self.grave7)

        grave_geometry8 = RectangleGeometry(2,3)
        grave_geometry8.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave8 = Mesh(grave_geometry8, grave_material)
        self.grave8.set_position([-91, -1.5, 20])
        self.scene.add(self.grave8)

        grave_geometry9 = RectangleGeometry(2,3)
        grave_geometry9.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave9 = Mesh(grave_geometry9, grave_material)
        self.grave9.set_position([-81, -1.5, -20])
        self.scene.add(self.grave9)

        grave_geometry10 = RectangleGeometry(2,3)
        grave_geometry10.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave10 = Mesh(grave_geometry10, grave_material)
        self.grave10.set_position([-81, -1.5, -15])
        self.scene.add(self.grave10)

        grave_geometry11 = RectangleGeometry(2,3)
        grave_geometry11.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave11 = Mesh(grave_geometry6, grave_material)
        self.grave11.set_position([-81, -1.5, -10])
        self.scene.add(self.grave6)

        grave_geometry12 = RectangleGeometry(2,3)
        grave_geometry12.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave12 = Mesh(grave_geometry12, grave_material)
        self.grave12.set_position([-81, -1.5, -5])
        self.scene.add(self.grave12)

        grave_geometry13 = RectangleGeometry(2,3)
        grave_geometry13.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave13 = Mesh(grave_geometry13, grave_material)
        self.grave13.set_position([-81, -1.5, 0])
        self.scene.add(self.grave13)

        grave_geometry14 = RectangleGeometry(2,3)
        grave_geometry14.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave14 = Mesh(grave_geometry14, grave_material)
        self.grave14.set_position([-81, -1.5, 5])
        self.scene.add(self.grave14)

        grave_geometry15 = RectangleGeometry(2,3)
        grave_geometry15.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave15 = Mesh(grave_geometry15, grave_material)
        self.grave15.set_position([-81, -1.5, 10])
        self.scene.add(self.grave15)

        grave_geometry16 = RectangleGeometry(2,3)
        grave_geometry16.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave16 = Mesh(grave_geometry16, grave_material)
        self.grave16.set_position([-81, -1.5, 15])
        self.scene.add(self.grave16)

        grave_geometry17 = RectangleGeometry(2,3)
        grave_geometry17.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.grave17 = Mesh(grave_geometry17, grave_material)
        self.grave17.set_position([-81, -1.5, 20])
        self.scene.add(self.grave17)

        lgrave_geometry = RectangleGeometry(2,3)
        lgrave_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave = Mesh(lgrave_geometry, grave_material)
        self.lgrave.set_position([-121, -1.5, -20])
        self.scene.add(self.lgrave)

        lgrave_geometry1 = RectangleGeometry(2,3)
        lgrave_geometry1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave1 = Mesh(lgrave_geometry1, grave_material)
        self.lgrave1.set_position([-121, -1.5, -15])
        self.scene.add(self.lgrave1)

        lgrave_geometry2 = RectangleGeometry(2,3)
        lgrave_geometry2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave2 = Mesh(lgrave_geometry2, grave_material)
        self.lgrave2.set_position([-111, -1.5, -10])
        self.scene.add(self.lgrave2)

        lgrave_geometry3 = RectangleGeometry(2,3)
        lgrave_geometry3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave3 = Mesh(lgrave_geometry3, grave_material)
        self.lgrave3.set_position([-111, -1.5, -5])
        self.scene.add(self.lgrave3)

        lgrave_geometry4 = RectangleGeometry(2,3)
        lgrave_geometry4.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave4 = Mesh(lgrave_geometry4, grave_material)
        self.lgrave4.set_position([-111, -1.5, 0])
        self.scene.add(self.lgrave4)

        lgrave_geometry5 = RectangleGeometry(2,3)
        lgrave_geometry5.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave5 = Mesh(lgrave_geometry5, grave_material)
        self.lgrave5.set_position([-111, -1.5, 5])
        self.scene.add(self.lgrave5)

        lgrave_geometry6 = RectangleGeometry(2,3)
        lgrave_geometry6.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave6 = Mesh(lgrave_geometry6, grave_material)
        self.lgrave6.set_position([-111, -1.5, 10])
        self.scene.add(self.lgrave6)

        lgrave_geometry7 = RectangleGeometry(2,3)
        lgrave_geometry7.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave7 = Mesh(lgrave_geometry7, grave_material)
        self.lgrave7.set_position([-111, -1.5, 15])
        self.scene.add(self.lgrave7)

        lgrave_geometry8 = RectangleGeometry(2,3)
        lgrave_geometry8.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave8 = Mesh(lgrave_geometry8, grave_material)
        self.lgrave8.set_position([-111, -1.5, 20])
        self.scene.add(self.lgrave8)

        lgrave_geometry9 = RectangleGeometry(2,3)
        lgrave_geometry9.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave9 = Mesh(lgrave_geometry9, grave_material)
        self.lgrave9.set_position([-121, -1.5, -20])
        self.scene.add(self.lgrave9)

        lgrave_geometry10 = RectangleGeometry(2,3)
        lgrave_geometry10.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave10 = Mesh(lgrave_geometry10, grave_material)
        self.lgrave10.set_position([-121, -1.5, -15])
        self.scene.add(self.lgrave10)

        lgrave_geometry11 = RectangleGeometry(2,3)
        lgrave_geometry11.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave11 = Mesh(lgrave_geometry6, grave_material)
        self.lgrave11.set_position([-121, -1.5, -10])
        self.scene.add(self.lgrave6)

        lgrave_geometry12 = RectangleGeometry(2,3)
        lgrave_geometry12.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave12 = Mesh(lgrave_geometry12, grave_material)
        self.lgrave12.set_position([-121, -1.5, -5])
        self.scene.add(self.lgrave12)

        lgrave_geometry13 = RectangleGeometry(2,3)
        lgrave_geometry13.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave13 = Mesh(lgrave_geometry13, grave_material)
        self.lgrave13.set_position([-121, -1.5, 0])
        self.scene.add(self.lgrave13)

        lgrave_geometry14 = RectangleGeometry(2,3)
        lgrave_geometry14.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave14 = Mesh(lgrave_geometry14, grave_material)
        self.lgrave14.set_position([-121, -1.5, 5])
        self.scene.add(self.lgrave14)

        lgrave_geometry15 = RectangleGeometry(2,3)
        lgrave_geometry15.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave15 = Mesh(lgrave_geometry15, grave_material)
        self.lgrave15.set_position([-121, -1.5, 10])
        self.scene.add(self.lgrave15)

        lgrave_geometry16 = RectangleGeometry(2,3)
        lgrave_geometry16.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave16 = Mesh(lgrave_geometry16, grave_material)
        self.lgrave16.set_position([-121, -1.5, 15])
        self.scene.add(self.lgrave16)

        lgrave_geometry17 = RectangleGeometry(2,3)
        lgrave_geometry17.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.lgrave17 = Mesh(lgrave_geometry17, grave_material)
        self.lgrave17.set_position([-121, -1.5, 20])
        self.scene.add(self.lgrave17)

        spookygate_material = TextureMaterial(texture=Texture(file_name="images/gate.png"))
        spookygate_geometry = RectangleGeometry(15,10)
        self.spookygate = Mesh(spookygate_geometry, spookygate_material)
        self.spookygate.set_position([-101, 0, -30])
        self.scene.add(self.spookygate)

        spookygate_material1 = TextureMaterial(texture=Texture(file_name="images/gate2.png"), property_dict={"doubleSide": True})
        spookygate_geometry1 = RectangleGeometry(15,10)
        self.spookygate1 = Mesh(spookygate_geometry1, spookygate_material1)
        self.spookygate1.set_position([-86.5, 0, -30])
        self.scene.add(self.spookygate1)

        spookygate_geometry2 = RectangleGeometry(15,10)
        self.spookygate2 = Mesh(spookygate_geometry2, spookygate_material1)
        self.spookygate2.set_position([-72, 0, -30])
        self.scene.add(self.spookygate2)

        spookygate_geometry3 = RectangleGeometry(15,10)
        self.spookygate3 = Mesh(spookygate_geometry3, spookygate_material1)
        self.spookygate3.set_position([-115.5, 0, -30])
        self.scene.add(self.spookygate3)

        spookygate_geometry4 = RectangleGeometry(15,10)
        self.spookygate4 = Mesh(spookygate_geometry4, spookygate_material1)
        self.spookygate4.set_position([-130, 0, -30])
        self.scene.add(self.spookygate4)

        spookygate_geometry5 = RectangleGeometry(15,10)
        self.spookygate5 = Mesh(spookygate_geometry5, spookygate_material1)
        self.spookygate5.set_position([-137.25, 0, -22.75])
        self.spookygate5.rotate_y(math.pi/2)
        self.scene.add(self.spookygate5)

        spookygate_geometry6 = RectangleGeometry(15,10)
        self.spookygate6 = Mesh(spookygate_geometry6, spookygate_material1)
        self.spookygate6.set_position([-64.75, 0, -22.75])
        self.spookygate6.rotate_y(math.pi/2)
        self.scene.add(self.spookygate6)

        spookygate_geometry7 = RectangleGeometry(15,10)
        self.spookygate7 = Mesh(spookygate_geometry7, spookygate_material1)
        self.spookygate7.set_position([-137.25, 0, -8.25])
        self.spookygate7.rotate_y(math.pi/2)
        self.scene.add(self.spookygate7)

        spookygate_geometry8 = RectangleGeometry(15,10)
        self.spookygate8 = Mesh(spookygate_geometry8, spookygate_material1)
        self.spookygate8.set_position([-64.75, 0, -8.25])
        self.spookygate8.rotate_y(math.pi/2)
        self.scene.add(self.spookygate8)

        spookygate_geometry9 = RectangleGeometry(15,10)
        self.spookygate9 = Mesh(spookygate_geometry9, spookygate_material1)
        self.spookygate9.set_position([-137.25, 0, 6.25])
        self.spookygate9.rotate_y(math.pi/2)
        self.scene.add(self.spookygate9)

        spookygate_geometry10 = RectangleGeometry(15,10)
        self.spookygate10 = Mesh(spookygate_geometry10, spookygate_material1)
        self.spookygate10.set_position([-64.75, 0, 6.25])
        self.spookygate10.rotate_y(math.pi/2)
        self.scene.add(self.spookygate10)

        spookygate_geometry11 = RectangleGeometry(15,10)
        self.spookygate11 = Mesh(spookygate_geometry11, spookygate_material1)
        self.spookygate11.set_position([-137.25, 0, 20.75])
        self.spookygate11.rotate_y(math.pi/2)
        self.scene.add(self.spookygate11)

        spookygate_geometry12 = RectangleGeometry(15,10)
        self.spookygate12 = Mesh(spookygate_geometry12, gate_material1)
        self.spookygate12.set_position([-64.75, 0, 20.75])
        self.spookygate12.rotate_y(math.pi/2)
        self.scene.add(self.spookygate12)

        spookygate_geometry13 = RectangleGeometry(15,10)
        self.spookygate13 = Mesh(spookygate_geometry13, spookygate_material1)
        self.spookygate13.set_position([-130, 0, 28])
        self.scene.add(self.spookygate13)

        spookygate_geometry14 = RectangleGeometry(15,10)
        self.spookygate14 = Mesh(spookygate_geometry14, spookygate_material1)
        self.spookygate14.set_position([-72, 0, 28])
        self.scene.add(self.spookygate14)

        spookygate_geometry15 = RectangleGeometry(15,10)
        self.spookygate15 = Mesh(spookygate_geometry15, spookygate_material1)
        self.spookygate15.set_position([-115.5, 0, 28])
        self.scene.add(self.spookygate15)

        spookygate_geometry16 = RectangleGeometry(15,10)
        self.spookygate16 = Mesh(spookygate_geometry16, spookygate_material1)
        self.spookygate16.set_position([-86.5, 0, 28])
        self.scene.add(self.spookygate16)

        spookygate_geometry17 = RectangleGeometry(15,10)
        self.spookygate17 = Mesh(spookygate_geometry17, spookygate_material1)
        self.spookygate17.set_position([-101, 0, 28])
        self.scene.add(self.spookygate17)

        zombie_material = TextureMaterial(texture=Texture(file_name="images/zombie.png"))
        zombie_geometry = RectangleGeometry(3,6)
        zombie_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.zombie = Mesh(zombie_geometry, zombie_material)
        self.zombie.set_position([-101, 0, 30])
        self.scene.add(self.zombie)


        #=================================================

        # SCENARIO LEVEL 5
        
        # obsidian_material = TextureMaterial(texture=Texture(file_name="images/obsidian.png"), property_dict={"repeatUV": [5, 5]})
        # tower_geometry = CylinderGeometry(height=6, radius=2, radial_segments=6)
        # self.tower_geometry = Mesh(tower_geometry, obsidian_material)
        # self.tower_geometry.set_position([10, 3.12, 0])
        # self.scene.add(self.tower_geometry)

        # tower_geometry1 = CylinderGeometry(height=10, radius=2, radial_segments=6)
        # self.tower1 = Mesh(tower_geometry1, obsidian_material)
        # self.tower1.set_position([15, 3.12, 10])
        # self.scene.add(self.tower1)

        # tower_geometry2 = CylinderGeometry(height=3, radius=2, radial_segments=6)
        # self.tower2 = Mesh(tower_geometry2, obsidian_material)
        # self.tower2.set_position([-10, 3.12, 0])
        # self.scene.add(self.tower2)

        # tower_geometry3 = CylinderGeometry(height=6, radius=2, radial_segments=6)
        # self.tower3 = Mesh(tower_geometry3, obsidian_material)
        # self.tower3.set_position([-15, 3.12, 10])
        # self.scene.add(self.tower3)

        # tower_geometry4 = CylinderGeometry(height=8, radius=2, radial_segments=6)
        # self.tower4 = Mesh(tower_geometry4, obsidian_material)
        # self.tower4.set_position([-15, 3.12, 20])
        # self.scene.add(self.tower4)

        # tower_geometry5 = CylinderGeometry(height=3, radius=2, radial_segments=6)
        # self.tower5 = Mesh(tower_geometry5, obsidian_material)
        # self.tower5.set_position([15, 3.12, 20])
        # self.scene.add(self.tower5)

        # tower_geometry6 = CylinderGeometry(height=3, radius=2, radial_segments=6)
        # self.tower6 = Mesh(tower_geometry6, obsidian_material)
        # self.tower6.set_position([-10, 3.12, 30])
        # self.scene.add(self.tower6)

        # tower_geometry7 = CylinderGeometry(height=10, radius=2, radial_segments=6)
        # self.tower7 = Mesh(tower_geometry7, obsidian_material)
        # self.tower7.set_position([0, 3.12, 30])
        # self.scene.add(self.tower7)

        # tower_geometry8 = CylinderGeometry(height=10, radius=2, radial_segments=6)
        # self.tower8 = Mesh(tower_geometry8, obsidian_material)
        # self.tower8.set_position([0, 3.12, -30])
        # self.scene.add(self.tower8)

        # tower_geometry9 = CylinderGeometry(height=10, radius=2, radial_segments=6)
        # self.tower9 = Mesh(tower_geometry9, obsidian_material)
        # self.tower9.set_position([10, 3.12, 30])
        # self.scene.add(self.tower9)

        self.scene.add(self.arrows[0])
        self.scene.add(self.arrows[1])
        self.scene.add(self.arrows[2])
        self.scene.add(self.target)
        self.scene.add(self.tripe)
        self.scene.add(self.mainPage)
        self.scene.add(self.instructions)
        self.scene.add(self.gameOver)
        self.scene.add(self.winning)

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
        self.tree.look_at(self.camera.global_position)
        self.tree1.look_at(self.camera.global_position)
        self.tree2.look_at(self.camera.global_position)
        self.tree3.look_at(self.camera.global_position)
        self.tree4.look_at(self.camera.global_position)
        self.tree5.look_at(self.camera.global_position)
        self.tree6.look_at(self.camera.global_position)
        self.tree7.look_at(self.camera.global_position)
        self.tree8.look_at(self.camera.global_position)
        
        self.grave.look_at(self.camera.global_position)
        self.grave1.look_at(self.camera.global_position)
        self.grave2.look_at(self.camera.global_position)
        self.grave3.look_at(self.camera.global_position)
        self.grave4.look_at(self.camera.global_position)
        self.grave5.look_at(self.camera.global_position)
        self.grave6.look_at(self.camera.global_position)
        self.grave7.look_at(self.camera.global_position)
        self.grave8.look_at(self.camera.global_position)
        self.grave9.look_at(self.camera.global_position)
        self.grave10.look_at(self.camera.global_position)
        self.grave11.look_at(self.camera.global_position)
        self.grave12.look_at(self.camera.global_position)
        self.grave13.look_at(self.camera.global_position)
        self.grave14.look_at(self.camera.global_position)
        self.grave15.look_at(self.camera.global_position)
        self.grave16.look_at(self.camera.global_position)
        self.grave17.look_at(self.camera.global_position)
        self.lgrave.look_at(self.camera.global_position)
        self.lgrave1.look_at(self.camera.global_position)
        self.lgrave2.look_at(self.camera.global_position)
        self.lgrave3.look_at(self.camera.global_position)
        self.lgrave4.look_at(self.camera.global_position)
        self.lgrave5.look_at(self.camera.global_position)
        self.lgrave6.look_at(self.camera.global_position)
        self.lgrave7.look_at(self.camera.global_position)
        self.lgrave8.look_at(self.camera.global_position)
        self.lgrave9.look_at(self.camera.global_position)
        self.lgrave10.look_at(self.camera.global_position)
        self.lgrave11.look_at(self.camera.global_position)
        self.lgrave12.look_at(self.camera.global_position)
        self.lgrave13.look_at(self.camera.global_position)
        self.lgrave14.look_at(self.camera.global_position)
        self.lgrave15.look_at(self.camera.global_position)
        self.lgrave16.look_at(self.camera.global_position)
        self.lgrave17.look_at(self.camera.global_position)

        self.camel.look_at(self.camera.global_position)
        self.camel1.look_at(self.camera.global_position)
        self.camel2.look_at(self.camera.global_position)
        self.camel3.look_at(self.camera.global_position)
        self.camel4.look_at(self.camera.global_position)
        
        self.palm.look_at(self.camera.global_position)
        self.palm1.look_at(self.camera.global_position)
        self.palm2.look_at(self.camera.global_position)
        self.palm3.look_at(self.camera.global_position)
        
        self.zombie.look_at(self.camera.global_position)

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
