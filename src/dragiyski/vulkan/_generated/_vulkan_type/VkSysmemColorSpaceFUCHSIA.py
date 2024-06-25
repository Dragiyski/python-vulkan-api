import ctypes

class VkSysmemColorSpaceFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorSpace', ctypes.c_uint32),
    ]

VkSysmemColorSpaceFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'colorSpace': ctypes.c_uint32,
}
