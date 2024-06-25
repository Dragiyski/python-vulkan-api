import ctypes

class VkQueueFamilyQueryResultStatusPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryResultStatusSupport', ctypes.c_uint32),
    ]

VkQueueFamilyQueryResultStatusPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queryResultStatusSupport': ctypes.c_uint32,
}
