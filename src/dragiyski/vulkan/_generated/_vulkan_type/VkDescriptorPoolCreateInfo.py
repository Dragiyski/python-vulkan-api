import ctypes

class VkDescriptorPoolCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'maxSets': ctypes.c_uint32,
            'poolSizeCount': ctypes.c_uint32,
            'pPoolSizes': ctypes.POINTER(VkDescriptorPoolSize),
        }


from .VkDescriptorPoolSize import VkDescriptorPoolSize

VkDescriptorPoolCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxSets', ctypes.c_uint32),
    ('poolSizeCount', ctypes.c_uint32),
    ('pPoolSizes', ctypes.POINTER(VkDescriptorPoolSize)),
]
