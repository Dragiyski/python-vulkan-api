import ctypes

class VkExtent2D(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
    ]

VkExtent2D._type_ = {
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
}
