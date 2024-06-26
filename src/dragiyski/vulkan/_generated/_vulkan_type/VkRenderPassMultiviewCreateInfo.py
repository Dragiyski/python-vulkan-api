import ctypes

class VkRenderPassMultiviewCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subpassCount', ctypes.c_uint32),
        ('pViewMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('dependencyCount', ctypes.c_uint32),
        ('pViewOffsets', ctypes.POINTER(ctypes.c_int32)),
        ('correlationMaskCount', ctypes.c_uint32),
        ('pCorrelationMasks', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkRenderPassCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'subpassCount': 'subpass_count',
        'pViewMasks': 'view_masks',
        'dependencyCount': 'dependency_count',
        'pViewOffsets': 'view_offsets',
        'correlationMaskCount': 'correlation_mask_count',
        'pCorrelationMasks': 'correlation_masks',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkRenderPassMultiviewCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subpassCount': ctypes.c_uint32,
    'pViewMasks': ctypes.POINTER(ctypes.c_uint32),
    'dependencyCount': ctypes.c_uint32,
    'pViewOffsets': ctypes.POINTER(ctypes.c_int32),
    'correlationMaskCount': ctypes.c_uint32,
    'pCorrelationMasks': ctypes.POINTER(ctypes.c_uint32),
}
