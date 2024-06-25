import ctypes

class VkPhysicalDeviceImageViewImageFormatInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageViewType', ctypes.c_int),
    ]

VkPhysicalDeviceImageViewImageFormatInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageViewType': ctypes.c_int,
}
