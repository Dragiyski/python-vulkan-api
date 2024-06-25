import ctypes

class VkPhysicalDeviceDynamicRenderingLocalReadFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicRenderingLocalRead', ctypes.c_uint32),
    ]

VkPhysicalDeviceDynamicRenderingLocalReadFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dynamicRenderingLocalRead': ctypes.c_uint32,
}
