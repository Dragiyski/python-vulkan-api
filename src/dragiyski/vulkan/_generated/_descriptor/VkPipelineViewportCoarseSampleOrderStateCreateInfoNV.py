from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'sampleOrderType', 'customSampleOrderCount', 'pCustomSampleOrders']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sampleOrderType': {
        'type': CIntType('c_int'),
        'type_name': 'VkCoarseSampleOrderTypeNV',
        'enum': 'VkCoarseSampleOrderTypeNV',
        'is_string': False,
    },
    'customSampleOrderCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCustomSampleOrders': {
        'type': CPointerType(CComplexType('VkCoarseSampleOrderCustomNV')),
        'type_name': 'VkCoarseSampleOrderCustomNV',
        'structure': 'VkCoarseSampleOrderCustomNV',
        'length': [['customSampleOrderCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineViewportStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkCoarseSampleOrderCustomNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
