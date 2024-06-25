import ctypes

class VkDescriptorPoolSize(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
    ]

VkDescriptorPoolSize._type_ = {
    'type': ctypes.c_int,
    'descriptorCount': ctypes.c_uint32,
}
