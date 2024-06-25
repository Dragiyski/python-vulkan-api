import ctypes

class VkPhysicalDeviceExternalFormatResolvePropertiesANDROID(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'nullColorAttachmentWithExternalFormatResolve': ctypes.c_uint32,
            'externalFormatResolveChromaOffsetX': ctypes.c_int,
            'externalFormatResolveChromaOffsetY': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nullColorAttachmentWithExternalFormatResolve', ctypes.c_uint32),
        ('externalFormatResolveChromaOffsetX', ctypes.c_int),
        ('externalFormatResolveChromaOffsetY', ctypes.c_int),
    ]
