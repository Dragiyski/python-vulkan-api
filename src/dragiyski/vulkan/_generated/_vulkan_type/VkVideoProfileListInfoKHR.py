import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoProfileInfoKHR import CType as VkVideoProfileInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('profileCount', ctypes.c_uint32),
    ('pProfiles', ctypes.POINTER(VkVideoProfileInfoKHR)),
]

descriptor = {
    'extends': {
        'VkBufferCreateInfo',
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
        'VkPhysicalDeviceVideoFormatInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoProfileInfoKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_PROFILE_LIST_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'profileCount': {'python_name': ['profile', 'count']},
        'pProfiles': {'python_name': ['p', 'profiles'], 'len': [['profileCount']], 'type': 'VkVideoProfileInfoKHR'},
    }
}
