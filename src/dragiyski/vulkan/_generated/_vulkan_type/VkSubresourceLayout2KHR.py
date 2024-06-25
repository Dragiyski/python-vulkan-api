import ctypes

class VkSubresourceLayout2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'subresourceLayout': VkSubresourceLayout,
        }


from .VkSubresourceLayout import VkSubresourceLayout

VkSubresourceLayout2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('subresourceLayout', VkSubresourceLayout),
]
