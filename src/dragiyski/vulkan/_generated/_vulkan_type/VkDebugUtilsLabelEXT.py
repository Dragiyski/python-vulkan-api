import ctypes

class VkDebugUtilsLabelEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pLabelName', ctypes.c_char_p),
        ('color', ctypes.ARRAY(ctypes.c_float, 4)),
    ]

VkDebugUtilsLabelEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pLabelName': ctypes.c_char_p,
    'color': ctypes.ARRAY(ctypes.c_float, 4),
}
