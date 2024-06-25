import ctypes

class VkSwapchainImageCreateInfoANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint32),
    ]

VkSwapchainImageCreateInfoANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'usage': ctypes.c_uint32,
}
