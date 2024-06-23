import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtensionProperties import CType as VkExtensionProperties
from .VkExtent2D import CType as VkExtent2D
from .VkVideoProfileInfoKHR import CType as VkVideoProfileInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyIndex', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('pVideoProfile', ctypes.POINTER(VkVideoProfileInfoKHR)),
    ('pictureFormat', ctypes.c_int),
    ('maxCodedExtent', VkExtent2D),
    ('referencePictureFormat', ctypes.c_int),
    ('maxDpbSlots', ctypes.c_uint32),
    ('maxActiveReferencePictures', ctypes.c_uint32),
    ('pStdHeaderVersion', ctypes.POINTER(VkExtensionProperties)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264SessionCreateInfoKHR',
        'VkVideoEncodeH265SessionCreateInfoKHR',
    },
    'includes': {
        'VkExtensionProperties',
        'VkExtent2D',
        'VkVideoProfileInfoKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateVideoSessionKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'queueFamilyIndex': {'python_name': ['queue', 'family', 'index']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoSessionCreateFlagsKHR'},
        'pVideoProfile': {'python_name': ['p', 'video', 'profile'], 'type': 'VkVideoProfileInfoKHR'},
        'pictureFormat': {'python_name': ['picture', 'format'], 'type': 'VkFormat'},
        'maxCodedExtent': {'python_name': ['max', 'coded', 'extent'], 'type': 'VkExtent2D'},
        'referencePictureFormat': {'python_name': ['reference', 'picture', 'format'], 'type': 'VkFormat'},
        'maxDpbSlots': {'python_name': ['max', 'dpb', 'slots']},
        'maxActiveReferencePictures': {'python_name': ['max', 'active', 'reference', 'pictures']},
        'pStdHeaderVersion': {'python_name': ['p', 'std', 'header', 'version'], 'type': 'VkExtensionProperties'},
    }
}
