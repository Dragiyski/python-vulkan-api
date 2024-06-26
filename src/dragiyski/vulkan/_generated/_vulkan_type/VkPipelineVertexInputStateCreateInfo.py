import ctypes

class VkPipelineVertexInputStateCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineVertexInputDivisorStateCreateInfoKHR',
    }
    _includes_ = {
        'VkVertexInputAttributeDescription',
        'VkVertexInputBindingDescription',
    }
    _included_in_ = {
        'VkGraphicsPipelineCreateInfo',
        'VkGraphicsShaderGroupCreateInfoNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'vertexBindingDescriptionCount': 'vertex_binding_description_count',
        'pVertexBindingDescriptions': 'vertex_binding_descriptions',
        'vertexAttributeDescriptionCount': 'vertex_attribute_description_count',
        'pVertexAttributeDescriptions': 'vertex_attribute_descriptions',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineVertexInputStateCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVertexInputAttributeDescription import VkVertexInputAttributeDescription
from .VkVertexInputBindingDescription import VkVertexInputBindingDescription

VkPipelineVertexInputStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('vertexBindingDescriptionCount', ctypes.c_uint32),
    ('pVertexBindingDescriptions', ctypes.POINTER(VkVertexInputBindingDescription)),
    ('vertexAttributeDescriptionCount', ctypes.c_uint32),
    ('pVertexAttributeDescriptions', ctypes.POINTER(VkVertexInputAttributeDescription)),
]

VkPipelineVertexInputStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'vertexBindingDescriptionCount': ctypes.c_uint32,
    'pVertexBindingDescriptions': ctypes.POINTER(VkVertexInputBindingDescription),
    'vertexAttributeDescriptionCount': ctypes.c_uint32,
    'pVertexAttributeDescriptions': ctypes.POINTER(VkVertexInputAttributeDescription),
}
