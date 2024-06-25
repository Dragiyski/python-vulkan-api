import ctypes

class VkPhysicalDeviceNestedCommandBufferPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxCommandBufferNestingLevel', ctypes.c_uint32),
    ]

VkPhysicalDeviceNestedCommandBufferPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxCommandBufferNestingLevel': ctypes.c_uint32,
}
