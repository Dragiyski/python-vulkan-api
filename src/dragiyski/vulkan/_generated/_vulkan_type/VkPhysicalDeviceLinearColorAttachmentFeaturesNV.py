import ctypes

class VkPhysicalDeviceLinearColorAttachmentFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('linearColorAttachment', ctypes.c_uint32),
    ]

VkPhysicalDeviceLinearColorAttachmentFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'linearColorAttachment': ctypes.c_uint32,
}
