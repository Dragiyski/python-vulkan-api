import ctypes, sys

class VkPipelineVertexInputStateCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineVertexInputStateCreateInfo

from . import VkVertexInputBindingDescription
from . import VkVertexInputAttributeDescription

VkPipelineVertexInputStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('vertexBindingDescriptionCount', ctypes.c_uint32),
    ('pVertexBindingDescriptions', ctypes.POINTER(VkVertexInputBindingDescription)),
    ('vertexAttributeDescriptionCount', ctypes.c_uint32),
    ('pVertexAttributeDescriptions', ctypes.POINTER(VkVertexInputAttributeDescription)),
]
