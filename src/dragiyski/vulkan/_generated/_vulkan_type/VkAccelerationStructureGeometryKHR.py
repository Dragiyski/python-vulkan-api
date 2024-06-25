import ctypes

class VkAccelerationStructureGeometryKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'geometryType': ctypes.c_int,
            'geometry': VkAccelerationStructureGeometryDataKHR,
            'flags': ctypes.c_uint32,
        }


from .VkAccelerationStructureGeometryDataKHR import VkAccelerationStructureGeometryDataKHR

VkAccelerationStructureGeometryKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkAccelerationStructureGeometryDataKHR),
    ('flags', ctypes.c_uint32),
]
