import ctypes

class VkPhysicalDeviceMaintenance4Properties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxBufferSize', ctypes.c_uint64),
    ]

VkPhysicalDeviceMaintenance4Properties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxBufferSize': ctypes.c_uint64,
}
