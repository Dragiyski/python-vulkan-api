import ctypes

class VkIndirectCommandsLayoutCreateInfoNV(ctypes.Structure):
    pass

from .VkIndirectCommandsLayoutTokenNV import VkIndirectCommandsLayoutTokenNV

VkIndirectCommandsLayoutCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('tokenCount', ctypes.c_uint32),
    ('pTokens', ctypes.POINTER(VkIndirectCommandsLayoutTokenNV)),
    ('streamCount', ctypes.c_uint32),
    ('pStreamStrides', ctypes.POINTER(ctypes.c_uint32)),
]

VkIndirectCommandsLayoutCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pipelineBindPoint': ctypes.c_int,
    'tokenCount': ctypes.c_uint32,
    'pTokens': ctypes.POINTER(VkIndirectCommandsLayoutTokenNV),
    'streamCount': ctypes.c_uint32,
    'pStreamStrides': ctypes.POINTER(ctypes.c_uint32),
}
