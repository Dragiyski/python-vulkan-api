import ctypes

class VkPushConstantRange(ctypes.Structure):
    _fields_ = [
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
    ]

VkPushConstantRange._type_ = {
    'stageFlags': ctypes.c_uint32,
    'offset': ctypes.c_uint32,
    'size': ctypes.c_uint32,
}
