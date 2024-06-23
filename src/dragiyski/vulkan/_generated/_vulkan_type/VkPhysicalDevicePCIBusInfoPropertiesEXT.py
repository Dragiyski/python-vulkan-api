import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pciDomain', ctypes.c_uint32),
        ('pciBus', ctypes.c_uint32),
        ('pciDevice', ctypes.c_uint32),
        ('pciFunction', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PCI_BUS_INFO_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pciDomain': {'python_name': ['pci', 'domain']},
        'pciBus': {'python_name': ['pci', 'bus']},
        'pciDevice': {'python_name': ['pci', 'device']},
        'pciFunction': {'python_name': ['pci', 'function']},
    }
}
