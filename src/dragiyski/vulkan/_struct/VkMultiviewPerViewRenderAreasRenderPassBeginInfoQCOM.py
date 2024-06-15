import ctypes, sys

class VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM

from . import VkRect2D

VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('perViewRenderAreaCount', ctypes.c_uint32),
    ('pPerViewRenderAreas', ctypes.POINTER(VkRect2D)),
]
