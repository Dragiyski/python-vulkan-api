import ctypes

class VkVideoPictureResourceInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkOffset2D',
    }
    _included_in_ = {
        'VkVideoDecodeInfoKHR',
        'VkVideoEncodeInfoKHR',
        'VkVideoReferenceSlotInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'codedOffset': 'coded_offset',
        'codedExtent': 'coded_extent',
        'baseArrayLayer': 'base_array_layer',
        'imageViewBinding': 'image_view_binding',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_PICTURE_RESOURCE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_PICTURE_RESOURCE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkVideoPictureResourceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('codedOffset', VkOffset2D),
    ('codedExtent', VkExtent2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('imageViewBinding', ctypes.c_void_p),
]

VkVideoPictureResourceInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'codedOffset': VkOffset2D,
    'codedExtent': VkExtent2D,
    'baseArrayLayer': ctypes.c_uint32,
    'imageViewBinding': ctypes.c_void_p,
}
