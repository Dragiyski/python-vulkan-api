import ctypes

class VkPhysicalDeviceVideoMaintenance1FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoMaintenance1', ctypes.c_uint32),
    ]

VkPhysicalDeviceVideoMaintenance1FeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'videoMaintenance1': ctypes.c_uint32,
}
