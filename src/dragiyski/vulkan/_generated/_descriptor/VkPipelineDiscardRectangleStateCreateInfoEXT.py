from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineDiscardRectangleStateCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'discardRectangleMode', 'discardRectangleCount', 'pDiscardRectangles']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineDiscardRectangleStateCreateFlagsEXT',
        'enum': 'VkPipelineDiscardRectangleStateCreateFlagsEXT',
        'is_string': False,
    },
    'discardRectangleMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkDiscardRectangleModeEXT',
        'enum': 'VkDiscardRectangleModeEXT',
        'is_string': False,
    },
    'discardRectangleCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDiscardRectangles': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['discardRectangleCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkGraphicsPipelineCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
