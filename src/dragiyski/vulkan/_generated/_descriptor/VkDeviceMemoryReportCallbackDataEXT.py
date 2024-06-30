from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceMemoryReportCallbackDataEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'type', 'memoryObjectId', 'size', 'objectType', 'objectHandle', 'heapIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDeviceMemoryReportFlagsEXT',
        'enum': 'VkDeviceMemoryReportFlagsEXT',
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkDeviceMemoryReportEventTypeEXT',
        'enum': 'VkDeviceMemoryReportEventTypeEXT',
        'is_string': False,
    },
    'memoryObjectId': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'type_name': 'VkObjectType',
        'enum': 'VkObjectType',
        'is_string': False,
    },
    'objectHandle': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'heapIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
