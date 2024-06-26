import ctypes

class VkOpticalFlowExecuteInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdOpticalFlowExecuteNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'regionCount': 'region_count',
        'pRegions': 'regions',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_optical_flow',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkOpticalFlowExecuteFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_EXECUTE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_EXECUTE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkOpticalFlowExecuteInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkRect2D)),
]

VkOpticalFlowExecuteInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkRect2D),
}
