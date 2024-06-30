from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkD3D12FenceSubmitInfoKHR'
_member_list_ = ['sType', 'pNext', 'waitSemaphoreValuesCount', 'pWaitSemaphoreValues', 'signalSemaphoreValuesCount', 'pSignalSemaphoreValues']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'waitSemaphoreValuesCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphoreValues': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['waitSemaphoreValuesCount']],
        'is_string': False,
    },
    'signalSemaphoreValuesCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSignalSemaphoreValues': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['signalSemaphoreValuesCount']],
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
