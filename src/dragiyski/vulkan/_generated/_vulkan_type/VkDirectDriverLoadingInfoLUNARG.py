import ctypes

class VkDirectDriverLoadingInfoLUNARG(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'pfnGetInstanceProcAddr': vkGetInstanceProcAddrLUNARG,
        }


from .._vulkan_callback.vkGetInstanceProcAddrLUNARG import vkGetInstanceProcAddrLUNARG

VkDirectDriverLoadingInfoLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnGetInstanceProcAddr', vkGetInstanceProcAddrLUNARG),
]
