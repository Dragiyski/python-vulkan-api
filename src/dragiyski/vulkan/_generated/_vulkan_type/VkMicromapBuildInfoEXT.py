import ctypes

class VkMicromapBuildInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'type': ctypes.c_int,
            'flags': ctypes.c_uint32,
            'mode': ctypes.c_int,
            'dstMicromap': ctypes.c_void_p,
            'usageCountsCount': ctypes.c_uint32,
            'pUsageCounts': ctypes.POINTER(VkMicromapUsageEXT),
            'ppUsageCounts': ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT)),
            'data': VkDeviceOrHostAddressConstKHR,
            'scratchData': VkDeviceOrHostAddressKHR,
            'triangleArray': VkDeviceOrHostAddressConstKHR,
            'triangleArrayStride': ctypes.c_uint64,
        }


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR
from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR
from .VkMicromapUsageEXT import VkMicromapUsageEXT

VkMicromapBuildInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('dstMicromap', ctypes.c_void_p),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('scratchData', VkDeviceOrHostAddressKHR),
    ('triangleArray', VkDeviceOrHostAddressConstKHR),
    ('triangleArrayStride', ctypes.c_uint64),
]
