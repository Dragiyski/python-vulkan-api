import ctypes, sys

class VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('graphicsPipelineLibraryFastLinking', ctypes.c_uint32),
        ('graphicsPipelineLibraryIndependentInterpolationDecoration', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT
