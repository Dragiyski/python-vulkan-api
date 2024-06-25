import ctypes

class VkPhysicalDevicePipelineLibraryGroupHandlesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineLibraryGroupHandles', ctypes.c_uint32),
    ]

VkPhysicalDevicePipelineLibraryGroupHandlesFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineLibraryGroupHandles': ctypes.c_uint32,
}
