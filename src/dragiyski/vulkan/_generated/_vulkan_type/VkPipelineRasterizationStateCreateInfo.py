import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('depthClampEnable', ctypes.c_uint32),
        ('rasterizerDiscardEnable', ctypes.c_uint32),
        ('polygonMode', ctypes.c_int),
        ('cullMode', ctypes.c_uint32),
        ('frontFace', ctypes.c_int),
        ('depthBiasEnable', ctypes.c_uint32),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
        ('lineWidth', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDepthBiasRepresentationInfoEXT',
        'VkPipelineRasterizationConservativeStateCreateInfoEXT',
        'VkPipelineRasterizationDepthClipStateCreateInfoEXT',
        'VkPipelineRasterizationLineStateCreateInfoKHR',
        'VkPipelineRasterizationProvokingVertexStateCreateInfoEXT',
        'VkPipelineRasterizationStateRasterizationOrderAMD',
        'VkPipelineRasterizationStateStreamCreateInfoEXT',
    },
    'includes': set(),
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineRasterizationStateCreateFlags'},
        'depthClampEnable': {'python_name': ['depth', 'clamp', 'enable']},
        'rasterizerDiscardEnable': {'python_name': ['rasterizer', 'discard', 'enable']},
        'polygonMode': {'python_name': ['polygon', 'mode'], 'type': 'VkPolygonMode'},
        'cullMode': {'python_name': ['cull', 'mode'], 'type': 'VkCullModeFlags'},
        'frontFace': {'python_name': ['front', 'face'], 'type': 'VkFrontFace'},
        'depthBiasEnable': {'python_name': ['depth', 'bias', 'enable']},
        'depthBiasConstantFactor': {'python_name': ['depth', 'bias', 'constant', 'factor']},
        'depthBiasClamp': {'python_name': ['depth', 'bias', 'clamp']},
        'depthBiasSlopeFactor': {'python_name': ['depth', 'bias', 'slope', 'factor']},
        'lineWidth': {'python_name': ['line', 'width']},
    }
}
