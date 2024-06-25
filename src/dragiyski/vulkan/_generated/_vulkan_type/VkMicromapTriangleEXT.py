import ctypes

class VkMicromapTriangleEXT(ctypes.Structure):
    _fields_ = [
        ('dataOffset', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint16),
        ('format', ctypes.c_uint16),
    ]

VkMicromapTriangleEXT._type_ = {
    'dataOffset': ctypes.c_uint32,
    'subdivisionLevel': ctypes.c_uint16,
    'format': ctypes.c_uint16,
}
