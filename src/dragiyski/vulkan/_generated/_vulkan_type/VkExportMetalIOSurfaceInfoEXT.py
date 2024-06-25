import ctypes

class VkExportMetalIOSurfaceInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('ioSurface', ctypes.c_void_p),
    ]

VkExportMetalIOSurfaceInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'image': ctypes.c_void_p,
    'ioSurface': ctypes.c_void_p,
}
