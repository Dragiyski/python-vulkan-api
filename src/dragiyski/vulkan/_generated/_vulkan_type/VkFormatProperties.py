import ctypes

class VkFormatProperties(ctypes.Structure):
    _fields_ = [
        ('linearTilingFeatures', ctypes.c_uint32),
        ('optimalTilingFeatures', ctypes.c_uint32),
        ('bufferFeatures', ctypes.c_uint32),
    ]

VkFormatProperties._type_ = {
    'linearTilingFeatures': ctypes.c_uint32,
    'optimalTilingFeatures': ctypes.c_uint32,
    'bufferFeatures': ctypes.c_uint32,
}
