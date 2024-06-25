import ctypes

class VkPhysicalDeviceRelaxedLineRasterizationFeaturesIMG(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('relaxedLineRasterization', ctypes.c_uint32),
    ]

VkPhysicalDeviceRelaxedLineRasterizationFeaturesIMG._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'relaxedLineRasterization': ctypes.c_uint32,
}
