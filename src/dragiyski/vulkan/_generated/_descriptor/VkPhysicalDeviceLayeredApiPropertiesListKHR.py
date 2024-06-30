from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceLayeredApiPropertiesListKHR'
_member_list_ = ['sType', 'pNext', 'layeredApiCount', 'pLayeredApis']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_PROPERTIES_LIST_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'layeredApiCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pLayeredApis': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceLayeredApiPropertiesKHR')),
        'type_name': 'VkPhysicalDeviceLayeredApiPropertiesKHR',
        'structure': 'VkPhysicalDeviceLayeredApiPropertiesKHR',
        'length': [['layeredApiCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = {
    'VkPhysicalDeviceLayeredApiPropertiesKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
