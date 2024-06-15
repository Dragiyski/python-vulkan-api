import ctypes, sys

class VkPhysicalDeviceTexelBufferAlignmentProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageTexelBufferOffsetAlignmentBytes', ctypes.c_uint64),
        ('storageTexelBufferOffsetSingleTexelAlignment', ctypes.c_uint32),
        ('uniformTexelBufferOffsetAlignmentBytes', ctypes.c_uint64),
        ('uniformTexelBufferOffsetSingleTexelAlignment', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceTexelBufferAlignmentProperties
