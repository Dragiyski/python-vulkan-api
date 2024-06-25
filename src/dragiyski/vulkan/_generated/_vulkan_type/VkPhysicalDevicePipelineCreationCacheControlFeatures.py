import ctypes

class VkPhysicalDevicePipelineCreationCacheControlFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineCreationCacheControl', ctypes.c_uint32),
    ]

VkPhysicalDevicePipelineCreationCacheControlFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineCreationCacheControl': ctypes.c_uint32,
}
