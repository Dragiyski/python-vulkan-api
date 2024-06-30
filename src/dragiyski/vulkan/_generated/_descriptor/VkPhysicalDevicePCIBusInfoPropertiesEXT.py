from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDevicePCIBusInfoPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'pciDomain', 'pciBus', 'pciDevice', 'pciFunction']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PCI_BUS_INFO_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pciDomain': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pciBus': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pciDevice': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pciFunction': {
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
