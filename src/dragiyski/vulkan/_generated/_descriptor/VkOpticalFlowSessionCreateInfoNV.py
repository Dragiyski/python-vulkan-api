from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOpticalFlowSessionCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'width', 'height', 'imageFormat', 'flowVectorFormat', 'costFormat', 'outputGridSize', 'hintGridSize', 'performanceLevel', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'flowVectorFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'costFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'outputGridSize': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowGridSizeFlagsNV',
        'enum': 'VkOpticalFlowGridSizeFlagsNV',
        'is_string': False,
    },
    'hintGridSize': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowGridSizeFlagsNV',
        'enum': 'VkOpticalFlowGridSizeFlagsNV',
        'is_string': False,
    },
    'performanceLevel': {
        'type': CIntType('c_int'),
        'type_name': 'VkOpticalFlowPerformanceLevelNV',
        'enum': 'VkOpticalFlowPerformanceLevelNV',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowSessionCreateFlagsNV',
        'enum': 'VkOpticalFlowSessionCreateFlagsNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkOpticalFlowSessionCreatePrivateDataInfoNV',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateOpticalFlowSessionNV',
}
_output_of_ = set()
