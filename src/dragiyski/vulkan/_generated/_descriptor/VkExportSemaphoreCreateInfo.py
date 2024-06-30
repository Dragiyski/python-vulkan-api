from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExportSemaphoreCreateInfo'
_member_list_ = ['sType', 'pNext', 'handleTypes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalSemaphoreHandleTypeFlags',
        'enum': 'VkExternalSemaphoreHandleTypeFlags',
        'is_string': False,
    },
}
_extends_ = {
    'VkSemaphoreCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
