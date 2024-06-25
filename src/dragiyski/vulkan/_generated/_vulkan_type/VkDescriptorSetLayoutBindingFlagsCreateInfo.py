import ctypes

class VkDescriptorSetLayoutBindingFlagsCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('bindingCount', ctypes.c_uint32),
        ('pBindingFlags', ctypes.POINTER(ctypes.c_uint32)),
    ]

VkDescriptorSetLayoutBindingFlagsCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'bindingCount': ctypes.c_uint32,
    'pBindingFlags': ctypes.POINTER(ctypes.c_uint32),
}
