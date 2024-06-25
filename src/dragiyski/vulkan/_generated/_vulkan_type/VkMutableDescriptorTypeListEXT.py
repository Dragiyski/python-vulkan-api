import ctypes

class VkMutableDescriptorTypeListEXT(ctypes.Structure):
    _fields_ = [
        ('descriptorTypeCount', ctypes.c_uint32),
        ('pDescriptorTypes', ctypes.POINTER(ctypes.c_int)),
    ]

VkMutableDescriptorTypeListEXT._type_ = {
    'descriptorTypeCount': ctypes.c_uint32,
    'pDescriptorTypes': ctypes.POINTER(ctypes.c_int),
}
