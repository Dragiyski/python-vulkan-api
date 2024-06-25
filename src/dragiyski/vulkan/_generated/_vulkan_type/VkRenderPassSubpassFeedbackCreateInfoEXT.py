import ctypes

class VkRenderPassSubpassFeedbackCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pSubpassFeedback': ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT),
        }


from .VkRenderPassSubpassFeedbackInfoEXT import VkRenderPassSubpassFeedbackInfoEXT

VkRenderPassSubpassFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pSubpassFeedback', ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]
