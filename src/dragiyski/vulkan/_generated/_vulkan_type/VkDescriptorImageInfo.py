import ctypes

class VkDescriptorImageInfo(ctypes.Structure):
    _fields_ = [
        ('sampler', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]

VkDescriptorImageInfo._type_ = {
    'sampler': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'imageLayout': ctypes.c_int,
}
