import ctypes

class VkImportMetalIOSurfaceInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('ioSurface', ctypes.c_void_p),
    ]

VkImportMetalIOSurfaceInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'ioSurface': ctypes.c_void_p,
}
