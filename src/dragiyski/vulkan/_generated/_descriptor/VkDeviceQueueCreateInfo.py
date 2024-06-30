from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceQueueCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'queueFamilyIndex', 'queueCount', 'pQueuePriorities']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDeviceQueueCreateFlags',
        'enum': 'VkDeviceQueueCreateFlags',
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'queueCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueuePriorities': {
        'type': CPointerType(CFloatType('c_float')),
        'length': [['queueCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDeviceQueueGlobalPriorityCreateInfoKHR',
    'VkDeviceQueueShaderCoreControlCreateInfoARM',
}
_includes_ = set()
_included_in_ = {
    'VkDeviceCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
