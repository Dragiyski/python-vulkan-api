from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassMultiviewCreateInfo'
_member_list_ = ['sType', 'pNext', 'subpassCount', 'pViewMasks', 'dependencyCount', 'pViewOffsets', 'correlationMaskCount', 'pCorrelationMasks']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subpassCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewMasks': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['subpassCount']],
        'is_string': False,
    },
    'dependencyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewOffsets': {
        'type': CPointerType(CIntType('c_int32')),
        'length': [['dependencyCount']],
        'is_string': False,
    },
    'correlationMaskCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCorrelationMasks': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['correlationMaskCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
