import ctypes, sys

class VkDirectDriverLoadingInfoLUNARG(ctypes.Structure):
    pass

sys.modules[__name__] = VkDirectDriverLoadingInfoLUNARG

from ..vulkan_callback import vkGetInstanceProcAddrLUNARG

VkDirectDriverLoadingInfoLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnGetInstanceProcAddr', ctypes.POINTER(vkGetInstanceProcAddrLUNARG)),
]
