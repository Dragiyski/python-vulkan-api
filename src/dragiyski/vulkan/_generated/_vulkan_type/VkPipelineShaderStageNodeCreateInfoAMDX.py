import ctypes

class VkPipelineShaderStageNodeCreateInfoAMDX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
        ('index', ctypes.c_uint32),
    ]

VkPipelineShaderStageNodeCreateInfoAMDX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
    'index': ctypes.c_uint32,
}
