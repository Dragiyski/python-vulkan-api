import ctypes

class VkPipelineColorBlendAdvancedStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
    ]

VkPipelineColorBlendAdvancedStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcPremultiplied': ctypes.c_uint32,
    'dstPremultiplied': ctypes.c_uint32,
    'blendOverlap': ctypes.c_int,
}
