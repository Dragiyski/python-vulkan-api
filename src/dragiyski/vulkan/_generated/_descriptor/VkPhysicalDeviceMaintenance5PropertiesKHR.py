from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMaintenance5PropertiesKHR'
_member_list_ = ['sType', 'pNext', 'earlyFragmentMultisampleCoverageAfterSampleCounting', 'earlyFragmentSampleMaskTestBeforeSampleCounting', 'depthStencilSwizzleOneSupport', 'polygonModePointSize', 'nonStrictSinglePixelWideLinesUseParallelogram', 'nonStrictWideLinesUseParallelogram']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_5_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'earlyFragmentMultisampleCoverageAfterSampleCounting': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'earlyFragmentSampleMaskTestBeforeSampleCounting': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depthStencilSwizzleOneSupport': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'polygonModePointSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'nonStrictSinglePixelWideLinesUseParallelogram': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'nonStrictWideLinesUseParallelogram': {
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
