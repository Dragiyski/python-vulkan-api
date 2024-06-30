from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShadingRateImagePropertiesNV'
_member_list_ = ['sType', 'pNext', 'shadingRateTexelSize', 'shadingRatePaletteSize', 'shadingRateMaxCoarseSamples']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shadingRateTexelSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'shadingRatePaletteSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shadingRateMaxCoarseSamples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
