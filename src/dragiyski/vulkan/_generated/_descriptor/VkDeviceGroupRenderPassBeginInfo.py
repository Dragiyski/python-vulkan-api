from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceGroupRenderPassBeginInfo'
_member_list_ = ['sType', 'pNext', 'deviceMask', 'deviceRenderAreaCount', 'pDeviceRenderAreas']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceRenderAreaCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDeviceRenderAreas': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['deviceRenderAreaCount']],
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
