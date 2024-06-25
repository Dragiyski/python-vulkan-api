import ctypes

class VkPushDescriptorSetInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stageFlags': ctypes.c_uint32,
            'layout': ctypes.c_void_p,
            'set': ctypes.c_uint32,
            'descriptorWriteCount': ctypes.c_uint32,
            'pDescriptorWrites': ctypes.POINTER(VkWriteDescriptorSet),
        }


from .VkWriteDescriptorSet import VkWriteDescriptorSet

VkPushDescriptorSetInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageFlags', ctypes.c_uint32),
    ('layout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
    ('descriptorWriteCount', ctypes.c_uint32),
    ('pDescriptorWrites', ctypes.POINTER(VkWriteDescriptorSet)),
]
