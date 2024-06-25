import ctypes

class VkMultiDrawInfoEXT(ctypes.Structure):
    _fields_ = [
        ('firstVertex', ctypes.c_uint32),
        ('vertexCount', ctypes.c_uint32),
    ]

VkMultiDrawInfoEXT._type_ = {
    'firstVertex': ctypes.c_uint32,
    'vertexCount': ctypes.c_uint32,
}
