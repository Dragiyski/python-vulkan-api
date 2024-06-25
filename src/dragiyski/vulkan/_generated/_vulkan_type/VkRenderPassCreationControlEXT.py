import ctypes

class VkRenderPassCreationControlEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('disallowMerging', ctypes.c_uint32),
    ]

VkRenderPassCreationControlEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'disallowMerging': ctypes.c_uint32,
}
