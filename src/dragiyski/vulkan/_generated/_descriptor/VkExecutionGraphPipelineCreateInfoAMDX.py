from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExecutionGraphPipelineCreateInfoAMDX'
_member_list_ = ['sType', 'pNext', 'flags', 'stageCount', 'pStages', 'pLibraryInfo', 'layout', 'basePipelineHandle', 'basePipelineIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXECUTION_GRAPH_PIPELINE_CREATE_INFO_AMDX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineCreateFlags',
        'enum': 'VkPipelineCreateFlags',
        'is_string': False,
    },
    'stageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStages': {
        'type': CPointerType(CComplexType('VkPipelineShaderStageCreateInfo')),
        'type_name': 'VkPipelineShaderStageCreateInfo',
        'structure': 'VkPipelineShaderStageCreateInfo',
        'length': [['stageCount']],
        'is_string': False,
    },
    'pLibraryInfo': {
        'type': CPointerType(CComplexType('VkPipelineLibraryCreateInfoKHR')),
        'type_name': 'VkPipelineLibraryCreateInfoKHR',
        'structure': 'VkPipelineLibraryCreateInfoKHR',
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'basePipelineHandle': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'basePipelineIndex': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineCompilerControlCreateInfoAMD',
    'VkPipelineCreationFeedbackCreateInfo',
}
_includes_ = {
    'VkPipelineLibraryCreateInfoKHR',
    'VkPipelineShaderStageCreateInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateExecutionGraphPipelinesAMDX',
}
_output_of_ = set()
