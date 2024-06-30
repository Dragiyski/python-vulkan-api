from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM'
_member_list_ = ['sType', 'pNext', 'perViewRenderAreaCount', 'pPerViewRenderAreas']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_RENDER_AREAS_RENDER_PASS_BEGIN_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'perViewRenderAreaCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPerViewRenderAreas': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['perViewRenderAreaCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassBeginInfo',
    'VkRenderingInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
