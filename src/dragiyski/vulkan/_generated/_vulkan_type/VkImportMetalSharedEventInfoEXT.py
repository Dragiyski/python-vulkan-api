import ctypes

class VkImportMetalSharedEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]

VkImportMetalSharedEventInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mtlSharedEvent': ctypes.c_void_p,
}
