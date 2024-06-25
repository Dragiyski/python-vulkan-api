import ctypes

class VkPhysicalDeviceSubpassMergeFeedbackFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subpassMergeFeedback', ctypes.c_uint32),
    ]

VkPhysicalDeviceSubpassMergeFeedbackFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subpassMergeFeedback': ctypes.c_uint32,
}
