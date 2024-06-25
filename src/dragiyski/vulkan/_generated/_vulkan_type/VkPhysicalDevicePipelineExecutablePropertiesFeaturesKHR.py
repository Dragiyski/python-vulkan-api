import ctypes

class VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineExecutableInfo', ctypes.c_uint32),
    ]

VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineExecutableInfo': ctypes.c_uint32,
}
