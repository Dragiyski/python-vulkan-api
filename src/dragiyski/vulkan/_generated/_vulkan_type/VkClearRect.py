import ctypes

class VkClearRect(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'rect': VkRect2D,
            'baseArrayLayer': ctypes.c_uint32,
            'layerCount': ctypes.c_uint32,
        }


from .VkRect2D import VkRect2D

VkClearRect._fields_ = [
    ('rect', VkRect2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
]
