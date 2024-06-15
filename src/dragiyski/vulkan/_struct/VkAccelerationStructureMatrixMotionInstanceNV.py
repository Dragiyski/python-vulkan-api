import ctypes, sys

class VkAccelerationStructureMatrixMotionInstanceNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureMatrixMotionInstanceNV

from . import VkTransformMatrixKHR

VkAccelerationStructureMatrixMotionInstanceNV._fields_ = [
    ('transformT0', VkTransformMatrixKHR),
    ('transformT1', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]
