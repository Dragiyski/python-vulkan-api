from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferMemoryBarrier'
_member_list_ = ['sType', 'pNext', 'srcAccessMask', 'dstAccessMask', 'srcQueueFamilyIndex', 'dstQueueFamilyIndex', 'buffer', 'offset', 'size']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcAccessMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccessFlags',
        'enum': 'VkAccessFlags',
        'is_string': False,
    },
    'dstAccessMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccessFlags',
        'enum': 'VkAccessFlags',
        'is_string': False,
    },
    'srcQueueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstQueueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkExternalMemoryAcquireUnmodifiedEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdPipelineBarrier',
    'vkCmdWaitEvents',
}
_output_of_ = set()
