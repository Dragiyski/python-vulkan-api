import ctypes

class VkPipelineViewportStateCreateInfo(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D
from .VkViewport import VkViewport

VkPipelineViewportStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewports', ctypes.POINTER(VkViewport)),
    ('scissorCount', ctypes.c_uint32),
    ('pScissors', ctypes.POINTER(VkRect2D)),
]

VkPipelineViewportStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pViewports': ctypes.POINTER(VkViewport),
    'scissorCount': ctypes.c_uint32,
    'pScissors': ctypes.POINTER(VkRect2D),
}
