import ctypes, sys

class VkPhysicalDeviceShaderIntegerDotProductProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('integerDotProduct8BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct8BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct8BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct4x8BitPackedUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct4x8BitPackedSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct4x8BitPackedMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct16BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct16BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct16BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct32BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct32BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct32BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct64BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct64BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct64BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating8BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating8BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating16BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating16BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating32BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating32BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating64BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating64BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderIntegerDotProductProperties