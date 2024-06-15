import ctypes, sys

class VkMutableDescriptorTypeListEXT(ctypes.Structure):
    _fields_ = [
        ('descriptorTypeCount', ctypes.c_uint32),
        ('pDescriptorTypes', ctypes.POINTER(ctypes.c_int)),
    ]

sys.modules[__name__] = VkMutableDescriptorTypeListEXT
