import ctypes

class VkPresentRegionKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkRectLayerKHR',
    }
    _included_in_ = {
        'VkPresentRegionsKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'rectangleCount': 'rectangle_count',
        'pRectangles': 'rectangles',
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


from .VkRectLayerKHR import VkRectLayerKHR

VkPresentRegionKHR._fields_ = [
    ('rectangleCount', ctypes.c_uint32),
    ('pRectangles', ctypes.POINTER(VkRectLayerKHR)),
]

VkPresentRegionKHR._type_ = {
    'rectangleCount': ctypes.c_uint32,
    'pRectangles': ctypes.POINTER(VkRectLayerKHR),
}
