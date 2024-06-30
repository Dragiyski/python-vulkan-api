from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceLayeredApiPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'vendorID', 'deviceID', 'layeredAPI', 'deviceName']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vendorID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layeredAPI': {
        'type': CIntType('c_int'),
        'type_name': 'VkPhysicalDeviceLayeredApiKHR',
        'enum': 'VkPhysicalDeviceLayeredApiKHR',
        'is_string': False,
    },
    'deviceName': {
        'type': CArrayType(CCharType('c_char'), 256),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPhysicalDeviceLayeredApiVulkanPropertiesKHR',
}
_includes_ = set()
_included_in_ = {
    'VkPhysicalDeviceLayeredApiPropertiesListKHR',
}
_input_of_ = set()
_output_of_ = set()
