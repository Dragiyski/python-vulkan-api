from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceExternalSemaphoreInfo'
_member_list_ = ['sType', 'pNext', 'handleType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalSemaphoreHandleTypeFlagBits',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkSemaphoreTypeCreateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceExternalSemaphoreProperties',
}
_output_of_ = set()
