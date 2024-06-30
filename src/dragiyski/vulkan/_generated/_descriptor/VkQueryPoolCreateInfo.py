from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueryPoolCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'queryType', 'queryCount', 'pipelineStatistics']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkQueryPoolCreateFlags',
        'enum': 'VkQueryPoolCreateFlags',
        'is_string': False,
    },
    'queryType': {
        'type': CIntType('c_int'),
        'type_name': 'VkQueryType',
        'enum': 'VkQueryType',
        'is_string': False,
    },
    'queryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pipelineStatistics': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkQueryPipelineStatisticFlags',
        'enum': 'VkQueryPipelineStatisticFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkQueryPoolPerformanceCreateInfoKHR',
    'VkQueryPoolPerformanceQueryCreateInfoINTEL',
    'VkQueryPoolVideoEncodeFeedbackCreateInfoKHR',
    'VkVideoDecodeAV1ProfileInfoKHR',
    'VkVideoDecodeH264ProfileInfoKHR',
    'VkVideoDecodeH265ProfileInfoKHR',
    'VkVideoDecodeUsageInfoKHR',
    'VkVideoEncodeH264ProfileInfoKHR',
    'VkVideoEncodeH265ProfileInfoKHR',
    'VkVideoEncodeUsageInfoKHR',
    'VkVideoProfileInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateQueryPool',
}
_output_of_ = set()
