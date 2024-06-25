import ctypes

class VkCudaFunctionCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('module', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
    ]

VkCudaFunctionCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'module': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
}
