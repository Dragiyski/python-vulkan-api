import ctypes

class VkPhysicalDeviceImagelessFramebufferFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imagelessFramebuffer', ctypes.c_uint32),
    ]

VkPhysicalDeviceImagelessFramebufferFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imagelessFramebuffer': ctypes.c_uint32,
}
