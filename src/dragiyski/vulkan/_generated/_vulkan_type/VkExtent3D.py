import ctypes

class VkExtent3D(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

VkExtent3D._type_ = {
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'depth': ctypes.c_uint32,
}
