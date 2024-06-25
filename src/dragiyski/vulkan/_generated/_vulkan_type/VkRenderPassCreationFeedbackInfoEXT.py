import ctypes

class VkRenderPassCreationFeedbackInfoEXT(ctypes.Structure):
    _fields_ = [
        ('postMergeSubpassCount', ctypes.c_uint32),
    ]

VkRenderPassCreationFeedbackInfoEXT._type_ = {
    'postMergeSubpassCount': ctypes.c_uint32,
}
