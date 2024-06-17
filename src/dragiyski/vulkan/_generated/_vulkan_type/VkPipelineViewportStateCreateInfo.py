import ctypes, sys

class VkPipelineViewportStateCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineViewportStateCreateInfo

from . import VkRect2D
from . import VkViewport

VkPipelineViewportStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewports', ctypes.POINTER(VkViewport)),
    ('scissorCount', ctypes.c_uint32),
    ('pScissors', ctypes.POINTER(VkRect2D)),
]
