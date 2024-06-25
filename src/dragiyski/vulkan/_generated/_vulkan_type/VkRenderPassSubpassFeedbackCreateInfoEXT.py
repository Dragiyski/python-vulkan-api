import ctypes

class VkRenderPassSubpassFeedbackCreateInfoEXT(ctypes.Structure):
    pass

from .VkRenderPassSubpassFeedbackInfoEXT import VkRenderPassSubpassFeedbackInfoEXT

VkRenderPassSubpassFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pSubpassFeedback', ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]

VkRenderPassSubpassFeedbackCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pSubpassFeedback': ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT),
}
