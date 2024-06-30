from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayPresentInfoKHR'
_member_list_ = ['sType', 'pNext', 'srcRect', 'dstRect', 'persistent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcRect': {
        'type': CComplexType('VkRect2D'),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'is_string': False,
    },
    'dstRect': {
        'type': CComplexType('VkRect2D'),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'is_string': False,
    },
    'persistent': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPresentInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
