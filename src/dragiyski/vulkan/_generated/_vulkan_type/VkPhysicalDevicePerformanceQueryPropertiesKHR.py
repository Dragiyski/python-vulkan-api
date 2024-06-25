import ctypes

class VkPhysicalDevicePerformanceQueryPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allowCommandBufferQueryCopies', ctypes.c_uint32),
    ]

VkPhysicalDevicePerformanceQueryPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'allowCommandBufferQueryCopies': ctypes.c_uint32,
}
