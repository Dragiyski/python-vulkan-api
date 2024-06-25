import ctypes

class VkCommandBufferInheritanceViewportScissorInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'viewportScissor2D': ctypes.c_uint32,
            'viewportDepthCount': ctypes.c_uint32,
            'pViewportDepths': ctypes.POINTER(VkViewport),
        }


from .VkViewport import VkViewport

VkCommandBufferInheritanceViewportScissorInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportScissor2D', ctypes.c_uint32),
    ('viewportDepthCount', ctypes.c_uint32),
    ('pViewportDepths', ctypes.POINTER(VkViewport)),
]
