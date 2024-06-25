import ctypes

class VkPipelineDynamicStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dynamicStateCount', ctypes.c_uint32),
        ('pDynamicStates', ctypes.POINTER(ctypes.c_int)),
    ]

VkPipelineDynamicStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dynamicStateCount': ctypes.c_uint32,
    'pDynamicStates': ctypes.POINTER(ctypes.c_int),
}
