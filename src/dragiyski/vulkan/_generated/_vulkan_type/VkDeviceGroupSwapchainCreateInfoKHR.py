import ctypes

class VkDeviceGroupSwapchainCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('modes', ctypes.c_uint32),
    ]

VkDeviceGroupSwapchainCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'modes': ctypes.c_uint32,
}
