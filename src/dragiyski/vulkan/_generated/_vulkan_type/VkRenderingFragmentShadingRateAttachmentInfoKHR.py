import ctypes

class VkRenderingFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'imageView': ctypes.c_void_p,
            'imageLayout': ctypes.c_int,
            'shadingRateAttachmentTexelSize': VkExtent2D,
        }


from .VkExtent2D import VkExtent2D

VkRenderingFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]
