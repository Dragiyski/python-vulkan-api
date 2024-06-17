import ctypes, sys

class VkSamplerYcbcrConversionImageFormatProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('combinedImageSamplerDescriptorCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSamplerYcbcrConversionImageFormatProperties
