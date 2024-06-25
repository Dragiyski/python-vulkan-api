import ctypes

class VkWriteDescriptorSetInlineUniformBlock(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dataSize', ctypes.c_uint32),
        ('pData', ctypes.c_void_p),
    ]

VkWriteDescriptorSetInlineUniformBlock._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dataSize': ctypes.c_uint32,
    'pData': ctypes.c_void_p,
}
