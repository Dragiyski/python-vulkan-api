import ctypes, sys

class VkAccelerationStructureSRTMotionInstanceNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureSRTMotionInstanceNV

from . import VkSRTDataNV

VkAccelerationStructureSRTMotionInstanceNV._fields_ = [
    ('transformT0', VkSRTDataNV),
    ('transformT1', VkSRTDataNV),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]
