import ctypes

class VkPhysicalDevicePipelineRobustnessFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineRobustness', ctypes.c_uint32),
    ]

VkPhysicalDevicePipelineRobustnessFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineRobustness': ctypes.c_uint32,
}
