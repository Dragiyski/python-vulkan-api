import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('descriptorTypeCount', ctypes.c_uint32),
        ('pDescriptorTypes', ctypes.POINTER(ctypes.c_int)),
    ]
