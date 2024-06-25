import ctypes

class VkPhysicalDeviceDiscardRectanglePropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxDiscardRectangles', ctypes.c_uint32),
    ]

VkPhysicalDeviceDiscardRectanglePropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxDiscardRectangles': ctypes.c_uint32,
}
