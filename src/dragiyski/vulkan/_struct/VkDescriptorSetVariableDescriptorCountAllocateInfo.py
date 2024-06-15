import ctypes, sys

class VkDescriptorSetVariableDescriptorCountAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pDescriptorCounts', ctypes.POINTER(ctypes.c_uint32)),
    ]

sys.modules[__name__] = VkDescriptorSetVariableDescriptorCountAllocateInfo
