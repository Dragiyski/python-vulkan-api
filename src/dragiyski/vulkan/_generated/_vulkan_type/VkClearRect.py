import ctypes

class VkClearRect(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkClearRect._fields_ = [
    ('rect', VkRect2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
]

VkClearRect._type_ = {
    'rect': VkRect2D,
    'baseArrayLayer': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
}
