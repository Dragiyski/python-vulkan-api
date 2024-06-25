import ctypes

class VkAccelerationStructureMemoryRequirementsInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('accelerationStructure', ctypes.c_void_p),
    ]

VkAccelerationStructureMemoryRequirementsInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'accelerationStructure': ctypes.c_void_p,
}
