import ctypes, sys

class VkAccelerationStructureTrianglesDisplacementMicromapNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureTrianglesDisplacementMicromapNV

from . import VkDeviceOrHostAddressConstKHR
from . import VkMicromapUsageEXT

VkAccelerationStructureTrianglesDisplacementMicromapNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displacementBiasAndScaleFormat', ctypes.c_int),
    ('displacementVectorFormat', ctypes.c_int),
    ('displacementBiasAndScaleBuffer', VkDeviceOrHostAddressConstKHR),
    ('displacementBiasAndScaleStride', ctypes.c_uint64),
    ('displacementVectorBuffer', VkDeviceOrHostAddressConstKHR),
    ('displacementVectorStride', ctypes.c_uint64),
    ('displacedMicromapPrimitiveFlags', VkDeviceOrHostAddressConstKHR),
    ('displacedMicromapPrimitiveFlagsStride', ctypes.c_uint64),
    ('indexType', ctypes.c_int),
    ('indexBuffer', VkDeviceOrHostAddressConstKHR),
    ('indexStride', ctypes.c_uint64),
    ('baseTriangle', ctypes.c_uint32),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('micromap', ctypes.c_void_p),
]
