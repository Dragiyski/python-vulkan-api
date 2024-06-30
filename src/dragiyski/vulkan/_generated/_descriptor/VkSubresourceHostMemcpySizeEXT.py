from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubresourceHostMemcpySizeEXT'
_member_list_ = ['sType', 'pNext', 'size']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBRESOURCE_HOST_MEMCPY_SIZE_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkSubresourceLayout2KHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
