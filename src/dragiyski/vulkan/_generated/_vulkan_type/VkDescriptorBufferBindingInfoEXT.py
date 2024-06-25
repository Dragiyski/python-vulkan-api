import ctypes

class VkDescriptorBufferBindingInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('address', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
    ]

VkDescriptorBufferBindingInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'address': ctypes.c_uint64,
    'usage': ctypes.c_uint32,
}
