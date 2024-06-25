import ctypes

class VkPhysicalDeviceTransformFeedbackFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('transformFeedback', ctypes.c_uint32),
        ('geometryStreams', ctypes.c_uint32),
    ]

VkPhysicalDeviceTransformFeedbackFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'transformFeedback': ctypes.c_uint32,
    'geometryStreams': ctypes.c_uint32,
}
