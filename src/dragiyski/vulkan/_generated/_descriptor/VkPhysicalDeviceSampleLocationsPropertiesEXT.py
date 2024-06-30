from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceSampleLocationsPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'sampleLocationSampleCounts', 'maxSampleLocationGridSize', 'sampleLocationCoordinateRange', 'sampleLocationSubPixelBits', 'variableSampleLocations']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sampleLocationSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'maxSampleLocationGridSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'sampleLocationCoordinateRange': {
        'type': CArrayType(CFloatType('c_float'), 2),
        'is_string': False,
    },
    'sampleLocationSubPixelBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'variableSampleLocations': {
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
