import ctypes

class VkPhysicalDeviceSamplerYcbcrConversionFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('samplerYcbcrConversion', ctypes.c_uint32),
    ]

VkPhysicalDeviceSamplerYcbcrConversionFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'samplerYcbcrConversion': ctypes.c_uint32,
}
