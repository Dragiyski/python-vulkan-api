import ctypes, sys

class VkPhysicalDeviceDepthBiasControlFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasControl', ctypes.c_uint32),
        ('leastRepresentableValueForceUnormRepresentation', ctypes.c_uint32),
        ('floatRepresentation', ctypes.c_uint32),
        ('depthBiasExact', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDepthBiasControlFeaturesEXT
