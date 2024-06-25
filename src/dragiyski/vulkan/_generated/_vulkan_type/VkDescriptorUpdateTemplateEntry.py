import ctypes

class VkDescriptorUpdateTemplateEntry(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'dstBinding': ctypes.c_uint32,
            'dstArrayElement': ctypes.c_uint32,
            'descriptorCount': ctypes.c_uint32,
            'descriptorType': ctypes.c_int,
            'offset': ctypes.c_size_t,
            'stride': ctypes.c_size_t,
        }

    _fields_ = [
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('offset', ctypes.c_size_t),
        ('stride', ctypes.c_size_t),
    ]
