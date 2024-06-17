import ctypes, sys

class VkPhysicalDeviceShaderTileImagePropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTileImageCoherentReadAccelerated', ctypes.c_uint32),
        ('shaderTileImageReadSampleFromPixelRateInvocation', ctypes.c_uint32),
        ('shaderTileImageReadFromHelperInvocation', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderTileImagePropertiesEXT
