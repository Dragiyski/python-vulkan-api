import ctypes

class VkDescriptorSetLayoutCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'bindingCount': ctypes.c_uint32,
            'pBindings': ctypes.POINTER(VkDescriptorSetLayoutBinding),
        }


from .VkDescriptorSetLayoutBinding import VkDescriptorSetLayoutBinding

VkDescriptorSetLayoutCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('bindingCount', ctypes.c_uint32),
    ('pBindings', ctypes.POINTER(VkDescriptorSetLayoutBinding)),
]
