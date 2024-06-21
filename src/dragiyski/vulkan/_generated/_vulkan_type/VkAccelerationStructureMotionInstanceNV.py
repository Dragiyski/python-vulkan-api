import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureMotionInstanceDataNV import CType as VkAccelerationStructureMotionInstanceDataNV

CType._fields_ = [
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('data', VkAccelerationStructureMotionInstanceDataNV),
]
