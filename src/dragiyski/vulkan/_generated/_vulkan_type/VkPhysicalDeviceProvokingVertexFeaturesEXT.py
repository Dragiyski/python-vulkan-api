import ctypes

class VkPhysicalDeviceProvokingVertexFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexLast', ctypes.c_uint32),
        ('transformFeedbackPreservesProvokingVertex', ctypes.c_uint32),
    ]

VkPhysicalDeviceProvokingVertexFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'provokingVertexLast': ctypes.c_uint32,
    'transformFeedbackPreservesProvokingVertex': ctypes.c_uint32,
}
