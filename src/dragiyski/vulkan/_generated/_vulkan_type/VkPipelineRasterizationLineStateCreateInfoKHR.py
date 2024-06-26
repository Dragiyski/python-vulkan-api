import ctypes

class VkPipelineRasterizationLineStateCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lineRasterizationMode', ctypes.c_int),
        ('stippledLineEnable', ctypes.c_uint32),
        ('lineStippleFactor', ctypes.c_uint32),
        ('lineStipplePattern', ctypes.c_uint16),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineRasterizationStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'lineRasterizationMode': 'line_rasterization_mode',
        'stippledLineEnable': 'stippled_line_enable',
        'lineStippleFactor': 'line_stipple_factor',
        'lineStipplePattern': 'line_stipple_pattern',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_line_rasterization',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'lineRasterizationMode': 'VkLineRasterizationModeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRasterizationLineStateCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'lineRasterizationMode': ctypes.c_int,
    'stippledLineEnable': ctypes.c_uint32,
    'lineStippleFactor': ctypes.c_uint32,
    'lineStipplePattern': ctypes.c_uint16,
}
