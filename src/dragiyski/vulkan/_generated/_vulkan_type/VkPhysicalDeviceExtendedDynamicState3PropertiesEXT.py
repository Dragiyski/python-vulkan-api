import ctypes

class VkPhysicalDeviceExtendedDynamicState3PropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicPrimitiveTopologyUnrestricted', ctypes.c_uint32),
    ]

VkPhysicalDeviceExtendedDynamicState3PropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dynamicPrimitiveTopologyUnrestricted': ctypes.c_uint32,
}
