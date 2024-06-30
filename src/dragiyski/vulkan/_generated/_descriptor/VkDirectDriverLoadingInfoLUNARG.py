from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDirectDriverLoadingInfoLUNARG'
_member_list_ = ['sType', 'pNext', 'flags', 'pfnGetInstanceProcAddr']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_INFO_LUNARG',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDirectDriverLoadingFlagsLUNARG',
        'enum': 'VkDirectDriverLoadingFlagsLUNARG',
        'is_string': False,
    },
    'pfnGetInstanceProcAddr': {
        'type': CFunctionType('vkGetInstanceProcAddrLUNARG'),
        'callback': 'vkGetInstanceProcAddrLUNARG',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDirectDriverLoadingListLUNARG',
}
_input_of_ = set()
_output_of_ = set()
