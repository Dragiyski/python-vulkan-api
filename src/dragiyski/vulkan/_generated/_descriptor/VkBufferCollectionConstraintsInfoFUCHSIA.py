from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferCollectionConstraintsInfoFUCHSIA'
_member_list_ = ['sType', 'pNext', 'minBufferCount', 'maxBufferCount', 'minBufferCountForCamping', 'minBufferCountForDedicatedSlack', 'minBufferCountForSharedSlack']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_CONSTRAINTS_INFO_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'minBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minBufferCountForCamping': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minBufferCountForDedicatedSlack': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minBufferCountForSharedSlack': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkBufferConstraintsInfoFUCHSIA',
    'VkImageConstraintsInfoFUCHSIA',
}
_input_of_ = set()
_output_of_ = set()
