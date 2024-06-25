import ctypes

class VkVideoFormatPropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'format': ctypes.c_int,
            'componentMapping': VkComponentMapping,
            'imageCreateFlags': ctypes.c_uint32,
            'imageType': ctypes.c_int,
            'imageTiling': ctypes.c_int,
            'imageUsageFlags': ctypes.c_uint32,
        }


from .VkComponentMapping import VkComponentMapping

VkVideoFormatPropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('componentMapping', VkComponentMapping),
    ('imageCreateFlags', ctypes.c_uint32),
    ('imageType', ctypes.c_int),
    ('imageTiling', ctypes.c_int),
    ('imageUsageFlags', ctypes.c_uint32),
]
