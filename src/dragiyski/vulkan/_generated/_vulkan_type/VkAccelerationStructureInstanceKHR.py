import ctypes

class CType(ctypes.Structure):
    pass

from .VkTransformMatrixKHR import CType as VkTransformMatrixKHR

CType._fields_ = [
    ('transform', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]
