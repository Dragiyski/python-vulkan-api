from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeQualityLevelPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'preferredRateControlMode', 'preferredRateControlLayerCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUALITY_LEVEL_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'preferredRateControlMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeRateControlModeFlagBitsKHR',
        'is_string': False,
    },
    'preferredRateControlLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264QualityLevelPropertiesKHR',
    'VkVideoEncodeH265QualityLevelPropertiesKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
}
