import ctypes

class VkCommandBufferInheritanceRenderPassTransformInfoQCOM(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkCommandBufferInheritanceInfo',
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
        'transform': 'transform',
        'renderArea': 'render_area',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_render_pass_transform',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDER_PASS_TRANSFORM_INFO_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDER_PASS_TRANSFORM_INFO_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkCommandBufferInheritanceRenderPassTransformInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('transform', ctypes.c_uint32),
    ('renderArea', VkRect2D),
]

VkCommandBufferInheritanceRenderPassTransformInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'transform': ctypes.c_uint32,
    'renderArea': VkRect2D,
}
