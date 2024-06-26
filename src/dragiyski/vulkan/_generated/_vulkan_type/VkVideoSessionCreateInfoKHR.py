import ctypes

class VkVideoSessionCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoEncodeH264SessionCreateInfoKHR',
        'VkVideoEncodeH265SessionCreateInfoKHR',
    }
    _includes_ = {
        'VkExtensionProperties',
        'VkExtent2D',
        'VkVideoProfileInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateVideoSessionKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'queueFamilyIndex': 'queue_family_index',
        'flags': 'flags',
        'pVideoProfile': 'video_profile',
        'pictureFormat': 'picture_format',
        'maxCodedExtent': 'max_coded_extent',
        'referencePictureFormat': 'reference_picture_format',
        'maxDpbSlots': 'max_dpb_slots',
        'maxActiveReferencePictures': 'max_active_reference_pictures',
        'pStdHeaderVersion': 'std_header_version',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoSessionCreateFlagsKHR',
        'pictureFormat': 'VkFormat',
        'referencePictureFormat': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_SESSION_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtensionProperties import VkExtensionProperties
from .VkExtent2D import VkExtent2D
from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

VkVideoSessionCreateInfoKHR._fields_ = [
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

VkVideoSessionCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queueFamilyIndex': ctypes.c_uint32,
    'flags': ctypes.c_uint32,
    'pVideoProfile': ctypes.POINTER(VkVideoProfileInfoKHR),
    'pictureFormat': ctypes.c_int,
    'maxCodedExtent': VkExtent2D,
    'referencePictureFormat': ctypes.c_int,
    'maxDpbSlots': ctypes.c_uint32,
    'maxActiveReferencePictures': ctypes.c_uint32,
    'pStdHeaderVersion': ctypes.POINTER(VkExtensionProperties),
}
