import ctypes

class VkImageViewSampleWeightCreateInfoQCOM(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkImageViewCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkOffset2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'filterCenter': 'filter_center',
        'filterSize': 'filter_size',
        'numPhases': 'num_phases',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_image_processing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_VIEW_SAMPLE_WEIGHT_CREATE_INFO_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_SAMPLE_WEIGHT_CREATE_INFO_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkImageViewSampleWeightCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('filterCenter', VkOffset2D),
    ('filterSize', VkExtent2D),
    ('numPhases', ctypes.c_uint32),
]

VkImageViewSampleWeightCreateInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'filterCenter': VkOffset2D,
    'filterSize': VkExtent2D,
    'numPhases': ctypes.c_uint32,
}
