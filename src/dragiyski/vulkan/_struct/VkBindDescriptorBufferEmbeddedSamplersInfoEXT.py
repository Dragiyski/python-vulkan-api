import ctypes, sys

class VkBindDescriptorBufferEmbeddedSamplersInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('set', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkBindDescriptorBufferEmbeddedSamplersInfoEXT
