import ctypes

class VkAccelerationStructureBuildGeometryInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'type': ctypes.c_int,
            'flags': ctypes.c_uint32,
            'mode': ctypes.c_int,
            'srcAccelerationStructure': ctypes.c_void_p,
            'dstAccelerationStructure': ctypes.c_void_p,
            'geometryCount': ctypes.c_uint32,
            'pGeometries': ctypes.POINTER(VkAccelerationStructureGeometryKHR),
            'ppGeometries': ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureGeometryKHR)),
            'scratchData': VkDeviceOrHostAddressKHR,
        }


from .VkAccelerationStructureGeometryKHR import VkAccelerationStructureGeometryKHR
from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR

VkAccelerationStructureBuildGeometryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('srcAccelerationStructure', ctypes.c_void_p),
    ('dstAccelerationStructure', ctypes.c_void_p),
    ('geometryCount', ctypes.c_uint32),
    ('pGeometries', ctypes.POINTER(VkAccelerationStructureGeometryKHR)),
    ('ppGeometries', ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureGeometryKHR))),
    ('scratchData', VkDeviceOrHostAddressKHR),
]
