import ctypes, sys

class VkRenderPassSubpassFeedbackCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassSubpassFeedbackCreateInfoEXT

from . import VkRenderPassSubpassFeedbackInfoEXT

VkRenderPassSubpassFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pSubpassFeedback', ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]
