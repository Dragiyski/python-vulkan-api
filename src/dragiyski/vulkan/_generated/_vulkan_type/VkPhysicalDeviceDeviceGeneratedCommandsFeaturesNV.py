import ctypes

class VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceGeneratedCommands', ctypes.c_uint32),
    ]

VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceGeneratedCommands': ctypes.c_uint32,
}
