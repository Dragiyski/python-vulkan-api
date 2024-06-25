import ctypes

class VkClearAttachment(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'aspectMask': ctypes.c_uint32,
            'colorAttachment': ctypes.c_uint32,
            'clearValue': VkClearValue,
        }


from .VkClearValue import VkClearValue

VkClearAttachment._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('colorAttachment', ctypes.c_uint32),
    ('clearValue', VkClearValue),
]
