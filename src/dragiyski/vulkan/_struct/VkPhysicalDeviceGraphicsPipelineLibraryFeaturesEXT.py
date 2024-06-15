import ctypes, sys

class VkPhysicalDeviceGraphicsPipelineLibraryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('graphicsPipelineLibrary', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceGraphicsPipelineLibraryFeaturesEXT
