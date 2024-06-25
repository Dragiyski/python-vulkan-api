import ctypes

class VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perViewPositionAllComponents', ctypes.c_uint32),
    ]

VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'perViewPositionAllComponents': ctypes.c_uint32,
}
