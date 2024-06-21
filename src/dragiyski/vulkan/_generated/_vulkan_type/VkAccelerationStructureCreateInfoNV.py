import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureInfoNV import CType as VkAccelerationStructureInfoNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('compactedSize', ctypes.c_uint64),
    ('info', VkAccelerationStructureInfoNV),
]
