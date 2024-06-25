import ctypes

class VkPhysicalDeviceProvokingVertexPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexModePerPipeline', ctypes.c_uint32),
        ('transformFeedbackPreservesTriangleFanProvokingVertex', ctypes.c_uint32),
    ]

VkPhysicalDeviceProvokingVertexPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'provokingVertexModePerPipeline': ctypes.c_uint32,
    'transformFeedbackPreservesTriangleFanProvokingVertex': ctypes.c_uint32,
}
