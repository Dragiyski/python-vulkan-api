import ctypes

class VkDeviceGroupRenderPassBeginInfo(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkDeviceGroupRenderPassBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceMask', ctypes.c_uint32),
    ('deviceRenderAreaCount', ctypes.c_uint32),
    ('pDeviceRenderAreas', ctypes.POINTER(VkRect2D)),
]

VkDeviceGroupRenderPassBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceMask': ctypes.c_uint32,
    'deviceRenderAreaCount': ctypes.c_uint32,
    'pDeviceRenderAreas': ctypes.POINTER(VkRect2D),
}
