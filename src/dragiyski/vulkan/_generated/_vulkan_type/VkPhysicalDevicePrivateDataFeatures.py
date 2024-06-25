import ctypes

class VkPhysicalDevicePrivateDataFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('privateData', ctypes.c_uint32),
    ]

VkPhysicalDevicePrivateDataFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'privateData': ctypes.c_uint32,
}
