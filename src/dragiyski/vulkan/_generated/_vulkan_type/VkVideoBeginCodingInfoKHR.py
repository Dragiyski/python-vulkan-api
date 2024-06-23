import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoReferenceSlotInfoKHR import CType as VkVideoReferenceSlotInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('videoSession', ctypes.c_void_p),
    ('videoSessionParameters', ctypes.c_void_p),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264GopRemainingFrameInfoKHR',
        'VkVideoEncodeH264RateControlInfoKHR',
        'VkVideoEncodeH265GopRemainingFrameInfoKHR',
        'VkVideoEncodeH265RateControlInfoKHR',
        'VkVideoEncodeRateControlInfoKHR',
    },
    'includes': {
        'VkVideoReferenceSlotInfoKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdBeginVideoCodingKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_BEGIN_CODING_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoBeginCodingFlagsKHR'},
        'videoSession': {'python_name': ['video', 'session']},
        'videoSessionParameters': {'python_name': ['video', 'session', 'parameters']},
        'referenceSlotCount': {'python_name': ['reference', 'slot', 'count']},
        'pReferenceSlots': {'python_name': ['p', 'reference', 'slots'], 'len': [['referenceSlotCount']], 'type': 'VkVideoReferenceSlotInfoKHR'},
    }
}
