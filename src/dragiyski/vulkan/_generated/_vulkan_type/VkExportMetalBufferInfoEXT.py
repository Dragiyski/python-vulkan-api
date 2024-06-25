import ctypes

class VkExportMetalBufferInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('mtlBuffer', ctypes.c_void_p),
    ]

VkExportMetalBufferInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memory': ctypes.c_void_p,
    'mtlBuffer': ctypes.c_void_p,
}
