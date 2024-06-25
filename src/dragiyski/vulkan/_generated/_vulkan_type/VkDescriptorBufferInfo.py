import ctypes

class VkDescriptorBufferInfo(ctypes.Structure):
    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]

VkDescriptorBufferInfo._type_ = {
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'range': ctypes.c_uint64,
}
