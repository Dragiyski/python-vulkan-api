import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('blockTexelViewCompatibleMultipleLayers', ctypes.c_uint32),
        ('maxCombinedImageSamplerDescriptorCount', ctypes.c_uint32),
        ('fragmentShadingRateClampCombinerInputs', ctypes.c_uint32),
    ]
