import ctypes

class VkDescriptorSetLayoutSupport(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supported', ctypes.c_uint32),
    ]

VkDescriptorSetLayoutSupport._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supported': ctypes.c_uint32,
}
