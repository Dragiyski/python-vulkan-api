import ctypes

class CType(ctypes.Structure):
    pass

from .VkConformanceVersion import CType as VkConformanceVersion

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('driverID', ctypes.c_int),
    ('driverName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('driverInfo', ctypes.ARRAY(ctypes.c_char, 256)),
    ('conformanceVersion', VkConformanceVersion),
]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkConformanceVersion',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'driverID': {'python_name': ['driver', 'id'], 'type': 'VkDriverId'},
        'driverName': {'python_name': ['driver', 'name'], 'len': [['null-terminated']]},
        'driverInfo': {'python_name': ['driver', 'info'], 'len': [['null-terminated']]},
        'conformanceVersion': {'python_name': ['conformance', 'version'], 'type': 'VkConformanceVersion'},
    }
}
