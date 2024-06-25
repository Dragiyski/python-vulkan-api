import ctypes

class VkCuModuleCreateInfoNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]

VkCuModuleCreateInfoNVX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dataSize': ctypes.c_size_t,
    'pData': ctypes.c_void_p,
}
