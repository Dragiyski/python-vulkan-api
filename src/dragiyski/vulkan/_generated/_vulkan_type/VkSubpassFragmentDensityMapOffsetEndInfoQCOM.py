import ctypes

class VkSubpassFragmentDensityMapOffsetEndInfoQCOM(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkSubpassEndInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkOffset2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'fragmentDensityOffsetCount': 'fragment_density_offset_count',
        'pFragmentDensityOffsets': 'fragment_density_offsets',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_fragment_density_map_offset',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBPASS_FRAGMENT_DENSITY_MAP_OFFSET_END_INFO_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_FRAGMENT_DENSITY_MAP_OFFSET_END_INFO_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkOffset2D import VkOffset2D

VkSubpassFragmentDensityMapOffsetEndInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetCount', ctypes.c_uint32),
    ('pFragmentDensityOffsets', ctypes.POINTER(VkOffset2D)),
]

VkSubpassFragmentDensityMapOffsetEndInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentDensityOffsetCount': ctypes.c_uint32,
    'pFragmentDensityOffsets': ctypes.POINTER(VkOffset2D),
}
