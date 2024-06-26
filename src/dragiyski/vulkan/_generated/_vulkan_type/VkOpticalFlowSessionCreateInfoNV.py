import ctypes

class VkOpticalFlowSessionCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('imageFormat', ctypes.c_int),
        ('flowVectorFormat', ctypes.c_int),
        ('costFormat', ctypes.c_int),
        ('outputGridSize', ctypes.c_uint32),
        ('hintGridSize', ctypes.c_uint32),
        ('performanceLevel', ctypes.c_int),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkOpticalFlowSessionCreatePrivateDataInfoNV',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateOpticalFlowSessionNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'width': 'width',
        'height': 'height',
        'imageFormat': 'image_format',
        'flowVectorFormat': 'flow_vector_format',
        'costFormat': 'cost_format',
        'outputGridSize': 'output_grid_size',
        'hintGridSize': 'hint_grid_size',
        'performanceLevel': 'performance_level',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_optical_flow',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'imageFormat': 'VkFormat',
        'flowVectorFormat': 'VkFormat',
        'costFormat': 'VkFormat',
        'outputGridSize': 'VkOpticalFlowGridSizeFlagsNV',
        'hintGridSize': 'VkOpticalFlowGridSizeFlagsNV',
        'performanceLevel': 'VkOpticalFlowPerformanceLevelNV',
        'flags': 'VkOpticalFlowSessionCreateFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkOpticalFlowSessionCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'imageFormat': ctypes.c_int,
    'flowVectorFormat': ctypes.c_int,
    'costFormat': ctypes.c_int,
    'outputGridSize': ctypes.c_uint32,
    'hintGridSize': ctypes.c_uint32,
    'performanceLevel': ctypes.c_int,
    'flags': ctypes.c_uint32,
}
