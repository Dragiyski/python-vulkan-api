import ctypes

class VkTransformMatrixKHR(ctypes.Structure):
    _fields_ = [
        ('matrix', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3)),
    ]

VkTransformMatrixKHR._type_ = {
    'matrix': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3),
}
