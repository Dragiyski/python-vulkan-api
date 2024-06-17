import ctypes, sys

class VkAccelerationStructureInstanceKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureInstanceKHR

from . import VkTransformMatrixKHR

VkAccelerationStructureInstanceKHR._fields_ = [
    ('transform', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]
