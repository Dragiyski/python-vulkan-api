import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoProfileInfoKHR import CType as VkVideoProfileInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pVideoProfile', ctypes.POINTER(VkVideoProfileInfoKHR)),
    ('qualityLevel', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkVideoProfileInfoKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_QUALITY_LEVEL_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pVideoProfile': {'python_name': ['p', 'video', 'profile'], 'type': 'VkVideoProfileInfoKHR'},
        'qualityLevel': {'python_name': ['quality', 'level']},
    }
}
