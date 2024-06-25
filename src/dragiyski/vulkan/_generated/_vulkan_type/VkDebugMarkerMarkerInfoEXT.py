import ctypes

class VkDebugMarkerMarkerInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pMarkerName', ctypes.c_char_p),
        ('color', ctypes.ARRAY(ctypes.c_float, 4)),
    ]

VkDebugMarkerMarkerInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pMarkerName': ctypes.c_char_p,
    'color': ctypes.ARRAY(ctypes.c_float, 4),
}
