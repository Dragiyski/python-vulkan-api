import ctypes

class VkIndirectCommandsLayoutTokenNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('tokenType', ctypes.c_int),
        ('stream', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('vertexBindingUnit', ctypes.c_uint32),
        ('vertexDynamicStride', ctypes.c_uint32),
        ('pushconstantPipelineLayout', ctypes.c_void_p),
        ('pushconstantShaderStageFlags', ctypes.c_uint32),
        ('pushconstantOffset', ctypes.c_uint32),
        ('pushconstantSize', ctypes.c_uint32),
        ('indirectStateFlags', ctypes.c_uint32),
        ('indexTypeCount', ctypes.c_uint32),
        ('pIndexTypes', ctypes.POINTER(ctypes.c_int)),
        ('pIndexTypeValues', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkIndirectCommandsLayoutCreateInfoNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'tokenType': 'token_type',
        'stream': 'stream',
        'offset': 'offset',
        'vertexBindingUnit': 'vertex_binding_unit',
        'vertexDynamicStride': 'vertex_dynamic_stride',
        'pushconstantPipelineLayout': 'pushconstant_pipeline_layout',
        'pushconstantShaderStageFlags': 'pushconstant_shader_stage_flags',
        'pushconstantOffset': 'pushconstant_offset',
        'pushconstantSize': 'pushconstant_size',
        'indirectStateFlags': 'indirect_state_flags',
        'indexTypeCount': 'index_type_count',
        'pIndexTypes': 'index_types',
        'pIndexTypeValues': 'index_type_values',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'tokenType': 'VkIndirectCommandsTokenTypeNV',
        'pushconstantShaderStageFlags': 'VkShaderStageFlags',
        'indirectStateFlags': 'VkIndirectStateFlagsNV',
        'pIndexTypes': 'VkIndexType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkIndirectCommandsLayoutTokenNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'tokenType': ctypes.c_int,
    'stream': ctypes.c_uint32,
    'offset': ctypes.c_uint32,
    'vertexBindingUnit': ctypes.c_uint32,
    'vertexDynamicStride': ctypes.c_uint32,
    'pushconstantPipelineLayout': ctypes.c_void_p,
    'pushconstantShaderStageFlags': ctypes.c_uint32,
    'pushconstantOffset': ctypes.c_uint32,
    'pushconstantSize': ctypes.c_uint32,
    'indirectStateFlags': ctypes.c_uint32,
    'indexTypeCount': ctypes.c_uint32,
    'pIndexTypes': ctypes.POINTER(ctypes.c_int),
    'pIndexTypeValues': ctypes.POINTER(ctypes.c_uint32),
}
