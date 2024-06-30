from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureDeviceAddressInfoKHR'
_member_list_ = ['sType', 'pNext', 'accelerationStructure']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_DEVICE_ADDRESS_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'accelerationStructure': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetAccelerationStructureDeviceAddressKHR',
}
_output_of_ = set()
