from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPresentIdKHR'
_member_list_ = ['sType', 'pNext', 'swapchainCount', 'pPresentIds']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PRESENT_ID_KHR',
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
    'pPresentIds': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['swapchainCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPresentInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
