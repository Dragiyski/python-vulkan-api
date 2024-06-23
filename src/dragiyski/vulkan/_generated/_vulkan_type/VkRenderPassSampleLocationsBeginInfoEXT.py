import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentSampleLocationsEXT import CType as VkAttachmentSampleLocationsEXT
from .VkSubpassSampleLocationsEXT import CType as VkSubpassSampleLocationsEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentInitialSampleLocationsCount', ctypes.c_uint32),
    ('pAttachmentInitialSampleLocations', ctypes.POINTER(VkAttachmentSampleLocationsEXT)),
    ('postSubpassSampleLocationsCount', ctypes.c_uint32),
    ('pPostSubpassSampleLocations', ctypes.POINTER(VkSubpassSampleLocationsEXT)),
]

descriptor = {
    'extends': {
        'VkRenderPassBeginInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkAttachmentSampleLocationsEXT',
        'VkSubpassSampleLocationsEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'attachmentInitialSampleLocationsCount': {'python_name': ['attachment', 'initial', 'sample', 'locations', 'count']},
        'pAttachmentInitialSampleLocations': {'python_name': ['p', 'attachment', 'initial', 'sample', 'locations'], 'len': [['attachmentInitialSampleLocationsCount']], 'type': 'VkAttachmentSampleLocationsEXT'},
        'postSubpassSampleLocationsCount': {'python_name': ['post', 'subpass', 'sample', 'locations', 'count']},
        'pPostSubpassSampleLocations': {'python_name': ['p', 'post', 'subpass', 'sample', 'locations'], 'len': [['postSubpassSampleLocationsCount']], 'type': 'VkSubpassSampleLocationsEXT'},
    }
}
