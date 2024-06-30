from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineVertexInputDivisorStateCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'vertexBindingDivisorCount', 'pVertexBindingDivisors']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexBindingDivisorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexBindingDivisors': {
        'type': CPointerType(CComplexType('VkVertexInputBindingDivisorDescriptionKHR')),
        'type_name': 'VkVertexInputBindingDivisorDescriptionKHR',
        'structure': 'VkVertexInputBindingDivisorDescriptionKHR',
        'length': [['vertexBindingDivisorCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineVertexInputStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkVertexInputBindingDivisorDescriptionKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
