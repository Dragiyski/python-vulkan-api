import ctypes, sys

class VkCommandBufferInheritanceConditionalRenderingInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('conditionalRenderingEnable', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkCommandBufferInheritanceConditionalRenderingInfoEXT
