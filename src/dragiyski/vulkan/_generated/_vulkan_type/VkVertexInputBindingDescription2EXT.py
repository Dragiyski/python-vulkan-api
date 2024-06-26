import ctypes

class VkVertexInputBindingDescription2EXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
        ('divisor', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetVertexInputEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'binding': 'binding',
        'stride': 'stride',
        'inputRate': 'input_rate',
        'divisor': 'divisor',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_shader_object',
        'VK_EXT_vertex_input_dynamic_state',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'inputRate': 'VkVertexInputRate',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VERTEX_INPUT_BINDING_DESCRIPTION_2_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VERTEX_INPUT_BINDING_DESCRIPTION_2_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkVertexInputBindingDescription2EXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'binding': ctypes.c_uint32,
    'stride': ctypes.c_uint32,
    'inputRate': ctypes.c_int,
    'divisor': ctypes.c_uint32,
}
