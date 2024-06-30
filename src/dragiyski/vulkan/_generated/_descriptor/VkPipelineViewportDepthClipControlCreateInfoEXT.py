from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportDepthClipControlCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'negativeOneToOne']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_DEPTH_CLIP_CONTROL_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'negativeOneToOne': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineViewportStateCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
