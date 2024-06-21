import ctypes

class CType(ctypes.Structure):
    pass

from .VkVertexInputBindingDivisorDescriptionKHR import CType as VkVertexInputBindingDivisorDescriptionKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexBindingDivisorCount', ctypes.c_uint32),
    ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR)),
]
