import ctypes

class VkFormatProperties3(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('linearTilingFeatures', ctypes.c_uint64),
        ('optimalTilingFeatures', ctypes.c_uint64),
        ('bufferFeatures', ctypes.c_uint64),
    ]

VkFormatProperties3._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'linearTilingFeatures': ctypes.c_uint64,
    'optimalTilingFeatures': ctypes.c_uint64,
    'bufferFeatures': ctypes.c_uint64,
}
