from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCommandBufferInheritanceViewportScissorInfoNV'
_member_list_ = ['sType', 'pNext', 'viewportScissor2D', 'viewportDepthCount', 'pViewportDepths']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_VIEWPORT_SCISSOR_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'viewportScissor2D': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'viewportDepthCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewportDepths': {
        'type': CPointerType(CComplexType('VkViewport')),
        'type_name': 'VkViewport',
        'structure': 'VkViewport',
        'is_string': False,
    },
}
_extends_ = {
    'VkCommandBufferInheritanceInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkViewport',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
