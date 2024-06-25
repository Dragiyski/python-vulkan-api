import ctypes

class VkAccelerationStructureGeometryMotionTrianglesDataNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'vertexData': VkDeviceOrHostAddressConstKHR,
        }


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryMotionTrianglesDataNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
]
