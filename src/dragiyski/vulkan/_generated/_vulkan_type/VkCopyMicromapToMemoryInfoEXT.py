import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressKHR import CType as VkDeviceOrHostAddressKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdCopyMicromapToMemoryEXT',
        'vkCopyMicromapToMemoryEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_MICROMAP_TO_MEMORY_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'src': {'python_name': ['src']},
        'dst': {'python_name': ['dst'], 'type': 'VkDeviceOrHostAddressKHR'},
        'mode': {'python_name': ['mode'], 'type': 'VkCopyMicromapModeEXT'},
    }
}
