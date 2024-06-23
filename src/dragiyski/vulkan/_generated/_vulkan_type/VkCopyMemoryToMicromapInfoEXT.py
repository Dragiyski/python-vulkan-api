import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdCopyMemoryToMicromapEXT',
        'vkCopyMemoryToMicromapEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_MICROMAP_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'src': {'python_name': ['src'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'dst': {'python_name': ['dst']},
        'mode': {'python_name': ['mode'], 'type': 'VkCopyMicromapModeEXT'},
    }
}
