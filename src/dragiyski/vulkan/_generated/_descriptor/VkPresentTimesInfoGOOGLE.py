from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPresentTimesInfoGOOGLE'
_member_list_ = ['sType', 'pNext', 'swapchainCount', 'pTimes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchainCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pTimes': {
        'type': CPointerType(CComplexType('VkPresentTimeGOOGLE')),
        'type_name': 'VkPresentTimeGOOGLE',
        'structure': 'VkPresentTimeGOOGLE',
        'length': [['swapchainCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPresentInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkPresentTimeGOOGLE',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
