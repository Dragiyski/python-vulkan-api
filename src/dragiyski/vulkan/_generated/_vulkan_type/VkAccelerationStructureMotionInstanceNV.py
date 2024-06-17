import ctypes, sys

class VkAccelerationStructureMotionInstanceNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureMotionInstanceNV

from . import VkAccelerationStructureMotionInstanceDataNV

VkAccelerationStructureMotionInstanceNV._fields_ = [
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('data', VkAccelerationStructureMotionInstanceDataNV),
]
