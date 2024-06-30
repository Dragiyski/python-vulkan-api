from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAmigoProfilingSubmitInfoSEC'
_member_list_ = ['sType', 'pNext', 'firstDrawTimestamp', 'swapBufferTimestamp']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_AMIGO_PROFILING_SUBMIT_INFO_SEC',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstDrawTimestamp': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'swapBufferTimestamp': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkSubmitInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
