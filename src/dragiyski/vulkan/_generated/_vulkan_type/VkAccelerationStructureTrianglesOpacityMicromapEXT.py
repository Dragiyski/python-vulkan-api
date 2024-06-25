import ctypes

class VkAccelerationStructureTrianglesOpacityMicromapEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'indexType': ctypes.c_int,
            'indexBuffer': VkDeviceOrHostAddressConstKHR,
            'indexStride': ctypes.c_uint64,
            'baseTriangle': ctypes.c_uint32,
            'usageCountsCount': ctypes.c_uint32,
            'pUsageCounts': ctypes.POINTER(VkMicromapUsageEXT),
            'ppUsageCounts': ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT)),
            'micromap': ctypes.c_void_p,
        }


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR
from .VkMicromapUsageEXT import VkMicromapUsageEXT

VkAccelerationStructureTrianglesOpacityMicromapEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('indexType', ctypes.c_int),
    ('indexBuffer', VkDeviceOrHostAddressConstKHR),
    ('indexStride', ctypes.c_uint64),
    ('baseTriangle', ctypes.c_uint32),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('micromap', ctypes.c_void_p),
]
