import ctypes, sys

class VkRenderPassCreationFeedbackInfoEXT(ctypes.Structure):
    _fields_ = [
        ('postMergeSubpassCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkRenderPassCreationFeedbackInfoEXT
