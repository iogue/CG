from core_ext.mesh import Mesh
from core_ext.texture import Texture

from math import pi

from core_ext.camera import Camera
from geometry.box import BoxGeometry
from geometry.cylinder import CylinderGeometry
from geometry.plane import PlaneGeometry
from geometry.polygon import PolygonGeometry
from geometry.pyramid import PyramidGeometry
from geometry.sphere import SphereGeometry
from geometry.rectangle import RectangleGeometry

from material.texture import TextureMaterial
from core.matrix import Matrix

class ScenarioMesh(Mesh):
    def __init__(self):
        mesh = RectangleGeometry(0,0)

        tree_geometry = RectangleGeometry(10,10)
        tree_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z

        tree_geometry1 = RectangleGeometry(10,10)
        tree_geometry1.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z

        tree_geometry2 = RectangleGeometry(10,10)
        tree_geometry2.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z

        tree_geometry3 = RectangleGeometry(10,10)
        tree_geometry3.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z

        tree_material = TextureMaterial(texture=Texture(file_name="images/tree.png"))

        self.mesh = super().__init__(mesh,tree_material)

        self.tree = Mesh(tree_geometry, tree_material)
        self.tree.set_position([-15, 3.25, -10])

        self.tree1 = Mesh(tree_geometry1, tree_material)
        self.tree1.set_position([15, 3.25, -10])

        self.tree2 = Mesh(tree_geometry2, tree_material)
        self.tree2.set_position([-10, 3.25, 0])

        self.tree3 = Mesh(tree_geometry3, tree_material)
        self.tree3.set_position([10, 3.25, 0])

        self.tree.look_at(self.camera.global_position)
        self.tree1.look_at(self.camera.global_position)
        self.tree2.look_at(self.camera.global_position)
        self.tree3.look_at(self.camera.global_position)

        self.add(self.tree)
        self.add(self.tree1)
        self.add(self.tree2)
        self.add(self.tree3)