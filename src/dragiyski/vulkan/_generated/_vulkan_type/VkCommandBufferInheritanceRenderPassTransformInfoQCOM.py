import ctypes, sys

class VkCommandBufferInheritanceRenderPassTransformInfoQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkCommandBufferInheritanceRenderPassTransformInfoQCOM

from . import VkRect2D

VkCommandBufferInheritanceRenderPassTransformInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('transform', ctypes.c_uint32),
    ('renderArea', VkRect2D),
]
