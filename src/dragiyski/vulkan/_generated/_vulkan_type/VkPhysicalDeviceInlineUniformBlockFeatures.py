import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
    ]
