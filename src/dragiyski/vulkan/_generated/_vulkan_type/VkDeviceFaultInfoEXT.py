import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceFaultAddressInfoEXT import CType as VkDeviceFaultAddressInfoEXT
from .VkDeviceFaultVendorInfoEXT import CType as VkDeviceFaultVendorInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pAddressInfos', ctypes.POINTER(VkDeviceFaultAddressInfoEXT)),
    ('pVendorInfos', ctypes.POINTER(VkDeviceFaultVendorInfoEXT)),
    ('pVendorBinaryData', ctypes.c_void_p),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceFaultAddressInfoEXT',
        'VkDeviceFaultVendorInfoEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDeviceFaultInfoEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'pAddressInfos': {'python_name': ['p', 'address', 'infos'], 'type': 'VkDeviceFaultAddressInfoEXT'},
        'pVendorInfos': {'python_name': ['p', 'vendor', 'infos'], 'type': 'VkDeviceFaultVendorInfoEXT'},
        'pVendorBinaryData': {'python_name': ['p', 'vendor', 'binary', 'data']},
    }
}
