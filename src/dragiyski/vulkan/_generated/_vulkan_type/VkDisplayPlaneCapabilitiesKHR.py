import ctypes

class VkDisplayPlaneCapabilitiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkOffset2D',
    }
    _included_in_ = {
        'VkDisplayPlaneCapabilities2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetDisplayPlaneCapabilitiesKHR',
    }
    _python_name_ = {
        'supportedAlpha': 'supported_alpha',
        'minSrcPosition': 'min_src_position',
        'maxSrcPosition': 'max_src_position',
        'minSrcExtent': 'min_src_extent',
        'maxSrcExtent': 'max_src_extent',
        'minDstPosition': 'min_dst_position',
        'maxDstPosition': 'max_dst_position',
        'minDstExtent': 'min_dst_extent',
        'maxDstExtent': 'max_dst_extent',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_display',
    }
    _vk_enum_ = {
        'supportedAlpha': 'VkDisplayPlaneAlphaFlagsKHR',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkDisplayPlaneCapabilitiesKHR._type_ = {
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
