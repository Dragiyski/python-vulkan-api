import ctypes, sys

class VkPhysicalDeviceFragmentShadingRateFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineFragmentShadingRate', ctypes.c_uint32),
        ('primitiveFragmentShadingRate', ctypes.c_uint32),
        ('attachmentFragmentShadingRate', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentShadingRateFeaturesKHR
