import ctypes

class VkSamplerYcbcrConversionInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('conversion', ctypes.c_void_p),
    ]

VkSamplerYcbcrConversionInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'conversion': ctypes.c_void_p,
}
