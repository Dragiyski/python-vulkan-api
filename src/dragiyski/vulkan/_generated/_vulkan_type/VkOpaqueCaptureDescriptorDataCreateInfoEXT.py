import ctypes

class VkOpaqueCaptureDescriptorDataCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opaqueCaptureDescriptorData', ctypes.c_void_p),
    ]

VkOpaqueCaptureDescriptorDataCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'opaqueCaptureDescriptorData': ctypes.c_void_p,
}
