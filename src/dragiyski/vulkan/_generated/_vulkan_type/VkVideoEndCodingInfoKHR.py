import ctypes

class VkVideoEndCodingInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdEndVideoCodingKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoEndCodingFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_END_CODING_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_END_CODING_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEndCodingInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
}
