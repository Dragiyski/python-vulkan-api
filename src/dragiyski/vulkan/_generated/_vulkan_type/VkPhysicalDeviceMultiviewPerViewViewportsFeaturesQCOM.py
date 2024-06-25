import ctypes

class VkPhysicalDeviceMultiviewPerViewViewportsFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiviewPerViewViewports', ctypes.c_uint32),
    ]

VkPhysicalDeviceMultiviewPerViewViewportsFeaturesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'multiviewPerViewViewports': ctypes.c_uint32,
}
