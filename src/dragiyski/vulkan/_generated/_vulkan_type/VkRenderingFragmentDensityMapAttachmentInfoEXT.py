import ctypes

class VkRenderingFragmentDensityMapAttachmentInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]

VkRenderingFragmentDensityMapAttachmentInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'imageLayout': ctypes.c_int,
}
