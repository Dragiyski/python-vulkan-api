import ctypes

class VkImageViewASTCDecodeModeEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('decodeMode', ctypes.c_int),
    ]

VkImageViewASTCDecodeModeEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'decodeMode': ctypes.c_int,
}
