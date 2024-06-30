from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkConditionalRenderingBeginInfoEXT'
_member_list_ = ['sType', 'pNext', 'buffer', 'offset', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
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
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkConditionalRenderingFlagsEXT',
        'enum': 'VkConditionalRenderingFlagsEXT',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdBeginConditionalRenderingEXT',
}
_output_of_ = set()
