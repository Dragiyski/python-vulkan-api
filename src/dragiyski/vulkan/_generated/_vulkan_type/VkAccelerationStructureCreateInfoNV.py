import ctypes, sys

class VkAccelerationStructureCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureCreateInfoNV

from . import VkAccelerationStructureInfoNV

VkAccelerationStructureCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('compactedSize', ctypes.c_uint64),
    ('info', VkAccelerationStructureInfoNV),
]
