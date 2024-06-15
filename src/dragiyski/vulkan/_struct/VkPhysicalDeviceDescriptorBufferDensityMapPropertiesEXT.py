import ctypes, sys

class VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('combinedImageSamplerDensityMapDescriptorSize', ctypes.c_size_t),
    ]

sys.modules[__name__] = VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT
