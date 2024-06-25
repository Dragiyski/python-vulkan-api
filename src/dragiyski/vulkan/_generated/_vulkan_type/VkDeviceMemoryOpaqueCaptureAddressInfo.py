import ctypes

class VkDeviceMemoryOpaqueCaptureAddressInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
    ]

VkDeviceMemoryOpaqueCaptureAddressInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memory': ctypes.c_void_p,
}
