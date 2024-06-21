import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('advancedBlendMaxColorAttachments', ctypes.c_uint32),
        ('advancedBlendIndependentBlend', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedSrcColor', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedDstColor', ctypes.c_uint32),
        ('advancedBlendCorrelatedOverlap', ctypes.c_uint32),
        ('advancedBlendAllOperations', ctypes.c_uint32),
    ]
