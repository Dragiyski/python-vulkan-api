import ctypes, sys

class VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShaderSampleInterlock', ctypes.c_uint32),
        ('fragmentShaderPixelInterlock', ctypes.c_uint32),
        ('fragmentShaderShadingRateInterlock', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT
