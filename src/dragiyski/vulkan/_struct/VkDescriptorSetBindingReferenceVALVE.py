import ctypes, sys

class VkDescriptorSetBindingReferenceVALVE(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorSetLayout', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDescriptorSetBindingReferenceVALVE
