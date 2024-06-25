import ctypes

class VkClearDepthStencilValue(ctypes.Structure):
    _fields_ = [
        ('depth', ctypes.c_float),
        ('stencil', ctypes.c_uint32),
    ]

VkClearDepthStencilValue._type_ = {
    'depth': ctypes.c_float,
    'stencil': ctypes.c_uint32,
}
