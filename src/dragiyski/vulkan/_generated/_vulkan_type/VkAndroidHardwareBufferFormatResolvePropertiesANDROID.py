import ctypes

class VkAndroidHardwareBufferFormatResolvePropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentFormat', ctypes.c_int),
    ]

VkAndroidHardwareBufferFormatResolvePropertiesANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'colorAttachmentFormat': ctypes.c_int,
}
