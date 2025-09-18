from abc import ABC, abstractmethod
from Vec3 import Point3, Vec3
from Ray import Ray
from Interval import Interval
from Material import Material

class HitRecord:
    def __init__(self):
        self.p = Point3()         # Hit point
        self.normal = Vec3()      # Surface normal at hit
        self.mat = None           # Material at hit
        self.t = 0.0              # Ray parameter at hit
        self.u = 0.0              # U texture coordinate
        self.v = 0.0              # V texture coordinate
        self.front_face = False   # Whether the hit was on the outside

    def set_face_normal(self, r, outward_normal):
        """
        Sets the hit record normal vector and determines if the hit was on the outside (front face).
        The parameter `outward_normal` is assumed to have unit length.
        """
        self.front_face = Vec3.dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        pass

    @abstractmethod
    def bounding_box(self):
        pass