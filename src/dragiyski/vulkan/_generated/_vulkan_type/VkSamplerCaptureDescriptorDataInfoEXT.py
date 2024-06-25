import ctypes

class VkSamplerCaptureDescriptorDataInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sampler', ctypes.c_void_p),
    ]

VkSamplerCaptureDescriptorDataInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampler': ctypes.c_void_p,
}
