import ctypes, sys

class VkPhysicalDeviceDescriptorBufferFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorBuffer', ctypes.c_uint32),
        ('descriptorBufferCaptureReplay', ctypes.c_uint32),
        ('descriptorBufferImageLayoutIgnored', ctypes.c_uint32),
        ('descriptorBufferPushDescriptors', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDescriptorBufferFeaturesEXT
