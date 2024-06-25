import ctypes

class VkDisplayPlaneCapabilitiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'supportedAlpha': ctypes.c_uint32,
            'minSrcPosition': VkOffset2D,
            'maxSrcPosition': VkOffset2D,
            'minSrcExtent': VkExtent2D,
            'maxSrcExtent': VkExtent2D,
            'minDstPosition': VkOffset2D,
            'maxDstPosition': VkOffset2D,
            'minDstExtent': VkExtent2D,
            'maxDstExtent': VkExtent2D,
        }


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkDisplayPlaneCapabilitiesKHR._fields_ = [
    ('supportedAlpha', ctypes.c_uint32),
    ('minSrcPosition', VkOffset2D),
    ('maxSrcPosition', VkOffset2D),
    ('minSrcExtent', VkExtent2D),
    ('maxSrcExtent', VkExtent2D),
    ('minDstPosition', VkOffset2D),
    ('maxDstPosition', VkOffset2D),
    ('minDstExtent', VkExtent2D),
    ('maxDstExtent', VkExtent2D),
]
