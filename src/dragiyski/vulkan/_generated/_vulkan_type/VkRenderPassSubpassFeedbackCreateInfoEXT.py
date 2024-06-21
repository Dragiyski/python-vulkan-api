import ctypes

class CType(ctypes.Structure):
    pass

from .VkRenderPassSubpassFeedbackInfoEXT import CType as VkRenderPassSubpassFeedbackInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pSubpassFeedback', ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]
