import ctypes

class VkDescriptorSetAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorPool', ctypes.c_void_p),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ]

VkDescriptorSetAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorPool': ctypes.c_void_p,
    'descriptorSetCount': ctypes.c_uint32,
    'pSetLayouts': ctypes.POINTER(ctypes.c_void_p),
}
