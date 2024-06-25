import ctypes

class VkOpticalFlowExecuteInfoNV(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkOpticalFlowExecuteInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkRect2D)),
]

VkOpticalFlowExecuteInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkRect2D),
}
