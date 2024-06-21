import ctypes

class CType(ctypes.Structure):
    pass

from .VkRenderPassCreationFeedbackInfoEXT import CType as VkRenderPassCreationFeedbackInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pRenderPassFeedback', ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT)),
]
