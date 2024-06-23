import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('codedOffset', VkOffset2D),
    ('codedExtent', VkExtent2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('imageViewBinding', ctypes.c_void_p),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkOffset2D',
    },
    'included_in': {
        'VkVideoDecodeInfoKHR',
        'VkVideoEncodeInfoKHR',
        'VkVideoReferenceSlotInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_PICTURE_RESOURCE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'codedOffset': {'python_name': ['coded', 'offset'], 'type': 'VkOffset2D'},
        'codedExtent': {'python_name': ['coded', 'extent'], 'type': 'VkExtent2D'},
        'baseArrayLayer': {'python_name': ['base', 'array', 'layer']},
        'imageViewBinding': {'python_name': ['image', 'view', 'binding']},
    }
}
