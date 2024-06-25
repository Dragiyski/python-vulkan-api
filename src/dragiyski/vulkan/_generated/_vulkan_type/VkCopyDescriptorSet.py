import ctypes

class VkCopyDescriptorSet(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcSet', ctypes.c_void_p),
        ('srcBinding', ctypes.c_uint32),
        ('srcArrayElement', ctypes.c_uint32),
        ('dstSet', ctypes.c_void_p),
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
    ]

VkCopyDescriptorSet._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSet': ctypes.c_void_p,
    'srcBinding': ctypes.c_uint32,
    'srcArrayElement': ctypes.c_uint32,
    'dstSet': ctypes.c_void_p,
    'dstBinding': ctypes.c_uint32,
    'dstArrayElement': ctypes.c_uint32,
    'descriptorCount': ctypes.c_uint32,
}
