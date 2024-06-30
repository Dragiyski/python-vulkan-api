from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceOpticalFlowPropertiesNV'
_member_list_ = ['sType', 'pNext', 'supportedOutputGridSizes', 'supportedHintGridSizes', 'hintSupported', 'costSupported', 'bidirectionalFlowSupported', 'globalFlowSupported', 'minWidth', 'minHeight', 'maxWidth', 'maxHeight', 'maxNumRegionsOfInterest']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPTICAL_FLOW_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'supportedOutputGridSizes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowGridSizeFlagsNV',
        'enum': 'VkOpticalFlowGridSizeFlagsNV',
        'is_string': False,
    },
    'supportedHintGridSizes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowGridSizeFlagsNV',
        'enum': 'VkOpticalFlowGridSizeFlagsNV',
        'is_string': False,
    },
    'hintSupported': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'costSupported': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bidirectionalFlowSupported': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'globalFlowSupported': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minWidth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minHeight': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxWidth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxHeight': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxNumRegionsOfInterest': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
