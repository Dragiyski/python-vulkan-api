import ctypes

class VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('perViewRenderAreaCount', ctypes.c_uint32),
    ('pPerViewRenderAreas', ctypes.POINTER(VkRect2D)),
]

VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'perViewRenderAreaCount': ctypes.c_uint32,
    'pPerViewRenderAreas': ctypes.POINTER(VkRect2D),
}
