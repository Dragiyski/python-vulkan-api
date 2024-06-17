import ctypes, sys

class VkAndroidHardwareBufferFormatResolvePropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentFormat', ctypes.c_int),
    ]

sys.modules[__name__] = VkAndroidHardwareBufferFormatResolvePropertiesANDROID
