from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceFragmentDensityMap2PropertiesEXT'
_member_list_ = ['sType', 'pNext', 'subsampledLoads', 'subsampledCoarseReconstructionEarlyAccess', 'maxSubsampledArrayLayers', 'maxDescriptorSetSubsampledSamplers']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subsampledLoads': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subsampledCoarseReconstructionEarlyAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxSubsampledArrayLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetSubsampledSamplers': {
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
