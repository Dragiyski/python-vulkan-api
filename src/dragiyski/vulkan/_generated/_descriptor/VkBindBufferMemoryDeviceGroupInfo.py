from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindBufferMemoryDeviceGroupInfo'
_member_list_ = ['sType', 'pNext', 'deviceIndexCount', 'pDeviceIndices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDeviceIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['deviceIndexCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkBindBufferMemoryInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
