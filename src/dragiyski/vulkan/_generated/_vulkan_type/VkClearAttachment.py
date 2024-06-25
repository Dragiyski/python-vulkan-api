import ctypes

class VkClearAttachment(ctypes.Structure):
    pass

from .VkClearValue import VkClearValue

VkClearAttachment._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('colorAttachment', ctypes.c_uint32),
    ('clearValue', VkClearValue),
]

VkClearAttachment._type_ = {
    'aspectMask': ctypes.c_uint32,
    'colorAttachment': ctypes.c_uint32,
    'clearValue': VkClearValue,
}
