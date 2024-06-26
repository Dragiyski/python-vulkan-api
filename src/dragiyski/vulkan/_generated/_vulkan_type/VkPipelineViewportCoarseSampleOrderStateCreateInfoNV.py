import ctypes

class VkPipelineViewportCoarseSampleOrderStateCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineViewportStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkCoarseSampleOrderCustomNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'sampleOrderType': 'sample_order_type',
        'customSampleOrderCount': 'custom_sample_order_count',
        'pCustomSampleOrders': 'custom_sample_orders',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_shading_rate_image',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'sampleOrderType': 'VkCoarseSampleOrderTypeNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkCoarseSampleOrderCustomNV import VkCoarseSampleOrderCustomNV

VkPipelineViewportCoarseSampleOrderStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleOrderType', ctypes.c_int),
    ('customSampleOrderCount', ctypes.c_uint32),
    ('pCustomSampleOrders', ctypes.POINTER(VkCoarseSampleOrderCustomNV)),
]

VkPipelineViewportCoarseSampleOrderStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleOrderType': ctypes.c_int,
    'customSampleOrderCount': ctypes.c_uint32,
    'pCustomSampleOrders': ctypes.POINTER(VkCoarseSampleOrderCustomNV),
}
