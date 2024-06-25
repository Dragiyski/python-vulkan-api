import ctypes

class VkPipelineViewportDepthClipControlCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('negativeOneToOne', ctypes.c_uint32),
    ]

VkPipelineViewportDepthClipControlCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'negativeOneToOne': ctypes.c_uint32,
}
