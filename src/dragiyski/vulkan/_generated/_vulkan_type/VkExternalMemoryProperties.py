import ctypes

class VkExternalMemoryProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'externalMemoryFeatures': ctypes.c_uint32,
            'exportFromImportedHandleTypes': ctypes.c_uint32,
            'compatibleHandleTypes': ctypes.c_uint32,
        }

    _fields_ = [
        ('externalMemoryFeatures', ctypes.c_uint32),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
    ]
