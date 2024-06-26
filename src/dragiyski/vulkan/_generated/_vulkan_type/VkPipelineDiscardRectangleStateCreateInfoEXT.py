import ctypes

class VkPipelineDiscardRectangleStateCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'discardRectangleMode': 'discard_rectangle_mode',
        'discardRectangleCount': 'discard_rectangle_count',
        'pDiscardRectangles': 'discard_rectangles',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_discard_rectangles',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineDiscardRectangleStateCreateFlagsEXT',
        'discardRectangleMode': 'VkDiscardRectangleModeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkPipelineDiscardRectangleStateCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('discardRectangleMode', ctypes.c_int),
    ('discardRectangleCount', ctypes.c_uint32),
    ('pDiscardRectangles', ctypes.POINTER(VkRect2D)),
]

VkPipelineDiscardRectangleStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'discardRectangleMode': ctypes.c_int,
    'discardRectangleCount': ctypes.c_uint32,
    'pDiscardRectangles': ctypes.POINTER(VkRect2D),
}
