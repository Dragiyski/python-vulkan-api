import ctypes

class CType(ctypes.Structure):
    pass

from .VkVertexInputAttributeDescription import CType as VkVertexInputAttributeDescription
from .VkVertexInputBindingDescription import CType as VkVertexInputBindingDescription

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('vertexBindingDescriptionCount', ctypes.c_uint32),
    ('pVertexBindingDescriptions', ctypes.POINTER(VkVertexInputBindingDescription)),
    ('vertexAttributeDescriptionCount', ctypes.c_uint32),
    ('pVertexAttributeDescriptions', ctypes.POINTER(VkVertexInputAttributeDescription)),
]
