import ctypes

class VkWriteDescriptorSetAccelerationStructureNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureCount', ctypes.c_uint32),
        ('pAccelerationStructures', ctypes.POINTER(ctypes.c_void_p)),
    ]

VkWriteDescriptorSetAccelerationStructureNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'accelerationStructureCount': ctypes.c_uint32,
    'pAccelerationStructures': ctypes.POINTER(ctypes.c_void_p),
}
