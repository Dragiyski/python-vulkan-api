from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyBufferInfo2'
_member_list_ = ['sType', 'pNext', 'srcBuffer', 'dstBuffer', 'regionCount', 'pRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_BUFFER_INFO_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'regionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRegions': {
        'type': CPointerType(CComplexType('VkBufferCopy2')),
        'type_name': 'VkBufferCopy2',
        'structure': 'VkBufferCopy2',
        'length': [['regionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBufferCopy2',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdCopyBuffer2',
}
_output_of_ = set()
