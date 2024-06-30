from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceAddressBindingCallbackDataEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'baseAddress', 'size', 'bindingType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_ADDRESS_BINDING_CALLBACK_DATA_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDeviceAddressBindingFlagsEXT',
        'enum': 'VkDeviceAddressBindingFlagsEXT',
        'is_string': False,
    },
    'baseAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'bindingType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDeviceAddressBindingTypeEXT',
        'enum': 'VkDeviceAddressBindingTypeEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkDebugUtilsMessengerCallbackDataEXT',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
