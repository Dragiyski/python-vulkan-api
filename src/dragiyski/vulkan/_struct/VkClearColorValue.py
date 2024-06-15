import ctypes, sys

class VkClearColorValue(ctypes.Union):
    _fields_ = [
        ('float32', ctypes.ARRAY(ctypes.c_float, 4)),
        ('int32', ctypes.ARRAY(ctypes.c_int32, 4)),
        ('uint32', ctypes.ARRAY(ctypes.c_uint32, 4)),
    ]

sys.modules[__name__] = VkClearColorValue
