import ctypes

class VkDescriptorGetInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'type': ctypes.c_int,
            'data': VkDescriptorDataEXT,
        }


from .VkDescriptorDataEXT import VkDescriptorDataEXT

VkDescriptorGetInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('data', VkDescriptorDataEXT),
]
