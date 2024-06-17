import ctypes, sys

class VkRenderPassCreationFeedbackCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassCreationFeedbackCreateInfoEXT

from . import VkRenderPassCreationFeedbackInfoEXT

VkRenderPassCreationFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pRenderPassFeedback', ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT)),
]
