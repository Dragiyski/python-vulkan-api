from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceFaultInfoEXT'
_member_list_ = ['sType', 'pNext', 'description', 'pAddressInfos', 'pVendorInfos', 'pVendorBinaryData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'pAddressInfos': {
        'type': CPointerType(CComplexType('VkDeviceFaultAddressInfoEXT')),
        'type_name': 'VkDeviceFaultAddressInfoEXT',
        'structure': 'VkDeviceFaultAddressInfoEXT',
        'is_string': False,
    },
    'pVendorInfos': {
        'type': CPointerType(CComplexType('VkDeviceFaultVendorInfoEXT')),
        'type_name': 'VkDeviceFaultVendorInfoEXT',
        'structure': 'VkDeviceFaultVendorInfoEXT',
        'is_string': False,
    },
    'pVendorBinaryData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDeviceFaultAddressInfoEXT',
    'VkDeviceFaultVendorInfoEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDeviceFaultInfoEXT',
}
