import ctypes, sys

class VkPhysicalDeviceExternalFormatResolvePropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nullColorAttachmentWithExternalFormatResolve', ctypes.c_uint32),
        ('externalFormatResolveChromaOffsetX', ctypes.c_int),
        ('externalFormatResolveChromaOffsetY', ctypes.c_int),
    ]

sys.modules[__name__] = VkPhysicalDeviceExternalFormatResolvePropertiesANDROID
