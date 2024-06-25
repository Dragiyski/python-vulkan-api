import ctypes

class VkPipelineVertexInputStateCreateInfo(ctypes.Structure):
    pass

from .VkVertexInputAttributeDescription import VkVertexInputAttributeDescription
from .VkVertexInputBindingDescription import VkVertexInputBindingDescription

VkPipelineVertexInputStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('vertexBindingDescriptionCount', ctypes.c_uint32),
    ('pVertexBindingDescriptions', ctypes.POINTER(VkVertexInputBindingDescription)),
    ('vertexAttributeDescriptionCount', ctypes.c_uint32),
    ('pVertexAttributeDescriptions', ctypes.POINTER(VkVertexInputAttributeDescription)),
]

VkPipelineVertexInputStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'vertexBindingDescriptionCount': ctypes.c_uint32,
    'pVertexBindingDescriptions': ctypes.POINTER(VkVertexInputBindingDescription),
    'vertexAttributeDescriptionCount': ctypes.c_uint32,
    'pVertexAttributeDescriptions': ctypes.POINTER(VkVertexInputAttributeDescription),
}
