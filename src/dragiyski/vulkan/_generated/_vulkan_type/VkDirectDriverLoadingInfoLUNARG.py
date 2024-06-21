import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkGetInstanceProcAddrLUNARG

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnGetInstanceProcAddr', vkGetInstanceProcAddrLUNARG),
]
