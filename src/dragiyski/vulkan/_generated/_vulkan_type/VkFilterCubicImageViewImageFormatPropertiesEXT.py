import ctypes

class VkFilterCubicImageViewImageFormatPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterCubic', ctypes.c_uint32),
        ('filterCubicMinmax', ctypes.c_uint32),
    ]

VkFilterCubicImageViewImageFormatPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'filterCubic': ctypes.c_uint32,
    'filterCubicMinmax': ctypes.c_uint32,
}
