import ctypes

class VkPhysicalDeviceOpacityMicromapPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxOpacity2StateSubdivisionLevel', ctypes.c_uint32),
        ('maxOpacity4StateSubdivisionLevel', ctypes.c_uint32),
    ]

VkPhysicalDeviceOpacityMicromapPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxOpacity2StateSubdivisionLevel': ctypes.c_uint32,
    'maxOpacity4StateSubdivisionLevel': ctypes.c_uint32,
}
