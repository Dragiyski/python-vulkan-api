from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceFaultFeaturesEXT'
_member_list_ = ['sType', 'pNext', 'deviceFault', 'deviceFaultVendorBinary']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FAULT_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceFault': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceFaultVendorBinary': {
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
