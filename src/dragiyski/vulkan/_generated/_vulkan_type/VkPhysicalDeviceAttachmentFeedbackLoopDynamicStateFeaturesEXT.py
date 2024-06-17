import ctypes, sys

class VkPhysicalDeviceAttachmentFeedbackLoopDynamicStateFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentFeedbackLoopDynamicState', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceAttachmentFeedbackLoopDynamicStateFeaturesEXT
