import ctypes

class VkMutableDescriptorTypeListEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'descriptorTypeCount': ctypes.c_uint32,
            'pDescriptorTypes': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('descriptorTypeCount', ctypes.c_uint32),
        ('pDescriptorTypes', ctypes.POINTER(ctypes.c_int)),
    ]
