import ctypes

class VkPhysicalDeviceAttachmentFeedbackLoopDynamicStateFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentFeedbackLoopDynamicState', ctypes.c_uint32),
    ]

VkPhysicalDeviceAttachmentFeedbackLoopDynamicStateFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentFeedbackLoopDynamicState': ctypes.c_uint32,
}
