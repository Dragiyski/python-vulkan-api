import ctypes

class VkPhysicalDeviceRobustness2PropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustStorageBufferAccessSizeAlignment', ctypes.c_uint64),
        ('robustUniformBufferAccessSizeAlignment', ctypes.c_uint64),
    ]

VkPhysicalDeviceRobustness2PropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'robustStorageBufferAccessSizeAlignment': ctypes.c_uint64,
    'robustUniformBufferAccessSizeAlignment': ctypes.c_uint64,
}
