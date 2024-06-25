import ctypes

class VkDescriptorBufferBindingPushDescriptorBufferHandleEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
    ]

VkDescriptorBufferBindingPushDescriptorBufferHandleEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'buffer': ctypes.c_void_p,
}
