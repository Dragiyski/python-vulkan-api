import ctypes

class VkShaderCreateInfoEXT(ctypes.Structure):
    pass

from .VkPushConstantRange import VkPushConstantRange
from .VkSpecializationInfo import VkSpecializationInfo

VkShaderCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('nextStage', ctypes.c_uint32),
    ('codeType', ctypes.c_int),
    ('codeSize', ctypes.c_size_t),
    ('pCode', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]

VkShaderCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stage': ctypes.c_uint32,
    'nextStage': ctypes.c_uint32,
    'codeType': ctypes.c_int,
    'codeSize': ctypes.c_size_t,
    'pCode': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
    'setLayoutCount': ctypes.c_uint32,
    'pSetLayouts': ctypes.POINTER(ctypes.c_void_p),
    'pushConstantRangeCount': ctypes.c_uint32,
    'pPushConstantRanges': ctypes.POINTER(VkPushConstantRange),
    'pSpecializationInfo': ctypes.POINTER(VkSpecializationInfo),
}
