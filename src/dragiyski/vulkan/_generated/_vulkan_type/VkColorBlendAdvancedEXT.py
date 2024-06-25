import ctypes

class VkColorBlendAdvancedEXT(ctypes.Structure):
    _fields_ = [
        ('advancedBlendOp', ctypes.c_int),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
        ('clampResults', ctypes.c_uint32),
    ]

VkColorBlendAdvancedEXT._type_ = {
    'advancedBlendOp': ctypes.c_int,
    'srcPremultiplied': ctypes.c_uint32,
    'dstPremultiplied': ctypes.c_uint32,
    'blendOverlap': ctypes.c_int,
    'clampResults': ctypes.c_uint32,
}
