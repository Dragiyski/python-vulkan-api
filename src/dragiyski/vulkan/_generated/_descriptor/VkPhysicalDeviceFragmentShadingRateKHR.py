from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceFragmentShadingRateKHR'
_member_list_ = ['sType', 'pNext', 'sampleCounts', 'fragmentSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'fragmentSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceFragmentShadingRatesKHR',
}
