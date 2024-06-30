from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR'
_member_list_ = ['sType', 'pNext', 'pVideoProfile', 'qualityLevel']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_QUALITY_LEVEL_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pVideoProfile': {
        'type': CPointerType(CComplexType('VkVideoProfileInfoKHR')),
        'type_name': 'VkVideoProfileInfoKHR',
        'structure': 'VkVideoProfileInfoKHR',
        'is_string': False,
    },
    'qualityLevel': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkVideoProfileInfoKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
}
_output_of_ = set()
