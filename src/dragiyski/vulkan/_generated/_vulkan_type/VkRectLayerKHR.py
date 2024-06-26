import ctypes

class VkRectLayerKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkOffset2D',
    }
    _included_in_ = {
        'VkPresentRegionKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'offset': 'offset',
        'extent': 'extent',
        'layer': 'layer',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_incremental_present',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkRectLayerKHR._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
    ('layer', ctypes.c_uint32),
]

VkRectLayerKHR._type_ = {
    'offset': VkOffset2D,
    'extent': VkExtent2D,
    'layer': ctypes.c_uint32,
}
