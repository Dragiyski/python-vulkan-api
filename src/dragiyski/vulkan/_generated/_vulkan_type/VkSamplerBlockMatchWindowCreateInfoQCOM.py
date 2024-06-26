import ctypes

class VkSamplerBlockMatchWindowCreateInfoQCOM(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkSamplerCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'windowExtent': 'window_extent',
        'windowCompareMode': 'window_compare_mode',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_image_processing2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'windowCompareMode': 'VkBlockMatchWindowCompareModeQCOM',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SAMPLER_BLOCK_MATCH_WINDOW_CREATE_INFO_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_BLOCK_MATCH_WINDOW_CREATE_INFO_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkSamplerBlockMatchWindowCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('windowExtent', VkExtent2D),
    ('windowCompareMode', ctypes.c_int),
]

VkSamplerBlockMatchWindowCreateInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'windowExtent': VkExtent2D,
    'windowCompareMode': ctypes.c_int,
}
