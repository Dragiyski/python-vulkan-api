import ctypes

class VkRenderPassCreationFeedbackCreateInfoEXT(ctypes.Structure):
    pass

from .VkRenderPassCreationFeedbackInfoEXT import VkRenderPassCreationFeedbackInfoEXT

VkRenderPassCreationFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pRenderPassFeedback', ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT)),
]

VkRenderPassCreationFeedbackCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pRenderPassFeedback': ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT),
}
