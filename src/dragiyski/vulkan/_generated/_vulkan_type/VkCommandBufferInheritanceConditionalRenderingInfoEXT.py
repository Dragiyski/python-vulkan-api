import ctypes

class VkCommandBufferInheritanceConditionalRenderingInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('conditionalRenderingEnable', ctypes.c_uint32),
    ]

VkCommandBufferInheritanceConditionalRenderingInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'conditionalRenderingEnable': ctypes.c_uint32,
}
