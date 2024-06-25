import ctypes

class VkPipelineTessellationStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('patchControlPoints', ctypes.c_uint32),
    ]

VkPipelineTessellationStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'patchControlPoints': ctypes.c_uint32,
}
