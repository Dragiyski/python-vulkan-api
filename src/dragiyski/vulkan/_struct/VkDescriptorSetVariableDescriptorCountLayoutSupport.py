import ctypes, sys

class VkDescriptorSetVariableDescriptorCountLayoutSupport(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxVariableDescriptorCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDescriptorSetVariableDescriptorCountLayoutSupport
