import ctypes, sys

class VkPhysicalDevicePipelineLibraryGroupHandlesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineLibraryGroupHandles', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelineLibraryGroupHandlesFeaturesEXT
