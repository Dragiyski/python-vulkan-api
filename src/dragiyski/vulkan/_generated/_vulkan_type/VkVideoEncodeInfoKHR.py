import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoPictureResourceInfoKHR import CType as VkVideoPictureResourceInfoKHR
from .VkVideoReferenceSlotInfoKHR import CType as VkVideoReferenceSlotInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstBuffer', ctypes.c_void_p),
    ('dstBufferOffset', ctypes.c_uint64),
    ('dstBufferRange', ctypes.c_uint64),
    ('srcPictureResource', VkVideoPictureResourceInfoKHR),
    ('pSetupReferenceSlot', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('precedingExternallyEncodedBytes', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264PictureInfoKHR',
        'VkVideoEncodeH265PictureInfoKHR',
        'VkVideoInlineQueryInfoKHR',
    },
    'includes': {
        'VkVideoPictureResourceInfoKHR',
        'VkVideoReferenceSlotInfoKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdEncodeVideoKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoEncodeFlagsKHR'},
        'dstBuffer': {'python_name': ['dst', 'buffer']},
        'dstBufferOffset': {'python_name': ['dst', 'buffer', 'offset']},
        'dstBufferRange': {'python_name': ['dst', 'buffer', 'range']},
        'srcPictureResource': {'python_name': ['src', 'picture', 'resource'], 'type': 'VkVideoPictureResourceInfoKHR'},
        'pSetupReferenceSlot': {'python_name': ['p', 'setup', 'reference', 'slot'], 'type': 'VkVideoReferenceSlotInfoKHR'},
        'referenceSlotCount': {'python_name': ['reference', 'slot', 'count']},
        'pReferenceSlots': {'python_name': ['p', 'reference', 'slots'], 'len': [['referenceSlotCount']], 'type': 'VkVideoReferenceSlotInfoKHR'},
        'precedingExternallyEncodedBytes': {'python_name': ['preceding', 'externally', 'encoded', 'bytes']},
    }
}
