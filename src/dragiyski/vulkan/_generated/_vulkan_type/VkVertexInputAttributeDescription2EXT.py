import ctypes

class VkVertexInputAttributeDescription2EXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]

VkVertexInputAttributeDescription2EXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'location': ctypes.c_uint32,
    'binding': ctypes.c_uint32,
    'format': ctypes.c_int,
    'offset': ctypes.c_uint32,
}
