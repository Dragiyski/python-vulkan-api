from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderClockFeaturesKHR'
_member_list_ = ['sType', 'pNext', 'shaderSubgroupClock', 'shaderDeviceClock']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CLOCK_FEATURES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderSubgroupClock': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDeviceClock': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
