import ctypes

class VkDepthBiasRepresentationInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasRepresentation', ctypes.c_int),
        ('depthBiasExact', ctypes.c_uint32),
    ]

VkDepthBiasRepresentationInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'depthBiasRepresentation': ctypes.c_int,
    'depthBiasExact': ctypes.c_uint32,
}
