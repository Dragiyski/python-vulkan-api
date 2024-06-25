import ctypes

class VkAccelerationStructureCreateInfoNV(ctypes.Structure):
    pass

from .VkAccelerationStructureInfoNV import VkAccelerationStructureInfoNV

VkAccelerationStructureCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('compactedSize', ctypes.c_uint64),
    ('info', VkAccelerationStructureInfoNV),
]

VkAccelerationStructureCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'compactedSize': ctypes.c_uint64,
    'info': VkAccelerationStructureInfoNV,
}
