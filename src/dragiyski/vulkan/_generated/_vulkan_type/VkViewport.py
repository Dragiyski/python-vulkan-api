import ctypes

class VkViewport(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
        ('width', ctypes.c_float),
        ('height', ctypes.c_float),
        ('minDepth', ctypes.c_float),
        ('maxDepth', ctypes.c_float),
    ]

VkViewport._type_ = {
    'x': ctypes.c_float,
    'y': ctypes.c_float,
    'width': ctypes.c_float,
    'height': ctypes.c_float,
    'minDepth': ctypes.c_float,
    'maxDepth': ctypes.c_float,
}
