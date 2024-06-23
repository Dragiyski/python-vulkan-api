import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoPictureResourceInfoKHR import CType as VkVideoPictureResourceInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('slotIndex', ctypes.c_int32),
    ('pPictureResource', ctypes.POINTER(VkVideoPictureResourceInfoKHR)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoDecodeAV1DpbSlotInfoKHR',
        'VkVideoDecodeH264DpbSlotInfoKHR',
        'VkVideoDecodeH265DpbSlotInfoKHR',
        'VkVideoEncodeH264DpbSlotInfoKHR',
        'VkVideoEncodeH265DpbSlotInfoKHR',
    },
    'includes': {
        'VkVideoPictureResourceInfoKHR',
    },
    'included_in': {
        'VkVideoBeginCodingInfoKHR',
        'VkVideoDecodeInfoKHR',
        'VkVideoEncodeInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_REFERENCE_SLOT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'slotIndex': {'python_name': ['slot', 'index']},
        'pPictureResource': {'python_name': ['p', 'picture', 'resource'], 'type': 'VkVideoPictureResourceInfoKHR'},
    }
}
