from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGetLatencyMarkerInfoNV'
_member_list_ = ['sType', 'pNext', 'timingCount', 'pTimings']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GET_LATENCY_MARKER_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'timingCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pTimings': {
        'type': CPointerType(CComplexType('VkLatencyTimingsFrameReportNV')),
        'type_name': 'VkLatencyTimingsFrameReportNV',
        'structure': 'VkLatencyTimingsFrameReportNV',
        'length': [['timingCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkLatencyTimingsFrameReportNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetLatencyTimingsNV',
}
