import ctypes, sys

class VkWriteDescriptorSetAccelerationStructureNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureCount', ctypes.c_uint32),
        ('pAccelerationStructures', ctypes.POINTER(ctypes.c_void_p)),
    ]

sys.modules[__name__] = VkWriteDescriptorSetAccelerationStructureNV
