import ctypes

class VkVideoPictureResourceInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'codedOffset': VkOffset2D,
            'codedExtent': VkExtent2D,
            'baseArrayLayer': ctypes.c_uint32,
            'imageViewBinding': ctypes.c_void_p,
        }


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkVideoPictureResourceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('codedOffset', VkOffset2D),
    ('codedExtent', VkExtent2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('imageViewBinding', ctypes.c_void_p),
]
