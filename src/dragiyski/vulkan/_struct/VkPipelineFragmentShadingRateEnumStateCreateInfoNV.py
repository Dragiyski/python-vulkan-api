import ctypes, sys

class VkPipelineFragmentShadingRateEnumStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shadingRateType', ctypes.c_int),
        ('shadingRate', ctypes.c_int),
        ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
    ]

sys.modules[__name__] = VkPipelineFragmentShadingRateEnumStateCreateInfoNV