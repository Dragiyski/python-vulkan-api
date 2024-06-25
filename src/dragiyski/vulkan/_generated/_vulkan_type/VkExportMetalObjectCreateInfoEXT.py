import ctypes

class VkExportMetalObjectCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exportObjectType', ctypes.c_uint32),
    ]

VkExportMetalObjectCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exportObjectType': ctypes.c_uint32,
}
