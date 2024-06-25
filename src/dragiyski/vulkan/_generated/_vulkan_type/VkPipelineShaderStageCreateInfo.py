import ctypes

class VkPipelineShaderStageCreateInfo(ctypes.Structure):
    pass

from .VkSpecializationInfo import VkSpecializationInfo

VkPipelineShaderStageCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('module', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]

VkPipelineShaderStageCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stage': ctypes.c_uint32,
    'module': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
    'pSpecializationInfo': ctypes.POINTER(VkSpecializationInfo),
}
