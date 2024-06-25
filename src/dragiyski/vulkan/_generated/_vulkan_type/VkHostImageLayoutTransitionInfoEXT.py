import ctypes

class VkHostImageLayoutTransitionInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'image': ctypes.c_void_p,
            'oldLayout': ctypes.c_int,
            'newLayout': ctypes.c_int,
            'subresourceRange': VkImageSubresourceRange,
        }


from .VkImageSubresourceRange import VkImageSubresourceRange

VkHostImageLayoutTransitionInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('image', ctypes.c_void_p),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('subresourceRange', VkImageSubresourceRange),
]
