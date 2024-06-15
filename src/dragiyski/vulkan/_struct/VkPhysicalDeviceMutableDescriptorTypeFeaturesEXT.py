import ctypes, sys

class VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mutableDescriptorType', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT
