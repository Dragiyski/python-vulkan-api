from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceQueueGlobalPriorityCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'globalPriority']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_GLOBAL_PRIORITY_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'globalPriority': {
        'type': CIntType('c_int'),
        'type_name': 'VkQueueGlobalPriorityKHR',
        'enum': 'VkQueueGlobalPriorityKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceQueueCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
