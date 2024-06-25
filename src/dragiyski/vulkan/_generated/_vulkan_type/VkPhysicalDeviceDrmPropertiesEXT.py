import ctypes

class VkPhysicalDeviceDrmPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasPrimary', ctypes.c_uint32),
        ('hasRender', ctypes.c_uint32),
        ('primaryMajor', ctypes.c_int64),
        ('primaryMinor', ctypes.c_int64),
        ('renderMajor', ctypes.c_int64),
        ('renderMinor', ctypes.c_int64),
    ]

VkPhysicalDeviceDrmPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hasPrimary': ctypes.c_uint32,
    'hasRender': ctypes.c_uint32,
    'primaryMajor': ctypes.c_int64,
    'primaryMinor': ctypes.c_int64,
    'renderMajor': ctypes.c_int64,
    'renderMinor': ctypes.c_int64,
}
