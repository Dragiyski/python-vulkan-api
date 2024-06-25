import ctypes

class VkCommandBufferInheritanceRenderPassTransformInfoQCOM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'transform': ctypes.c_uint32,
            'renderArea': VkRect2D,
        }


from .VkRect2D import VkRect2D

VkCommandBufferInheritanceRenderPassTransformInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('transform', ctypes.c_uint32),
    ('renderArea', VkRect2D),
]
