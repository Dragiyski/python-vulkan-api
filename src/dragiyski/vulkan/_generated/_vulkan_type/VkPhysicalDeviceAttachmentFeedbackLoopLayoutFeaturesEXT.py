import ctypes

class VkPhysicalDeviceAttachmentFeedbackLoopLayoutFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentFeedbackLoopLayout', ctypes.c_uint32),
    ]

VkPhysicalDeviceAttachmentFeedbackLoopLayoutFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentFeedbackLoopLayout': ctypes.c_uint32,
}
