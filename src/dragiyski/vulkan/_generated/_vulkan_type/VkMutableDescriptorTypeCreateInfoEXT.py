import ctypes

class VkMutableDescriptorTypeCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'mutableDescriptorTypeListCount': ctypes.c_uint32,
            'pMutableDescriptorTypeLists': ctypes.POINTER(VkMutableDescriptorTypeListEXT),
        }


from .VkMutableDescriptorTypeListEXT import VkMutableDescriptorTypeListEXT

VkMutableDescriptorTypeCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mutableDescriptorTypeListCount', ctypes.c_uint32),
    ('pMutableDescriptorTypeLists', ctypes.POINTER(VkMutableDescriptorTypeListEXT)),
]
