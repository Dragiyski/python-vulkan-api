from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalSemaphoreProperties'
_member_list_ = ['sType', 'pNext', 'exportFromImportedHandleTypes', 'compatibleHandleTypes', 'externalSemaphoreFeatures']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'exportFromImportedHandleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalSemaphoreHandleTypeFlags',
        'enum': 'VkExternalSemaphoreHandleTypeFlags',
        'is_string': False,
    },
    'compatibleHandleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalSemaphoreHandleTypeFlags',
        'enum': 'VkExternalSemaphoreHandleTypeFlags',
        'is_string': False,
    },
    'externalSemaphoreFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalSemaphoreFeatureFlags',
        'enum': 'VkExternalSemaphoreFeatureFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceExternalSemaphoreProperties',
}
