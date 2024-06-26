import ctypes

class VkVideoEncodeUsageInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoUsageHints', ctypes.c_uint32),
        ('videoContentHints', ctypes.c_uint32),
        ('tuningMode', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkQueryPoolCreateInfo',
        'VkVideoProfileInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'videoUsageHints': 'video_usage_hints',
        'videoContentHints': 'video_content_hints',
        'tuningMode': 'tuning_mode',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'videoUsageHints': 'VkVideoEncodeUsageFlagsKHR',
        'videoContentHints': 'VkVideoEncodeContentFlagsKHR',
        'tuningMode': 'VkVideoEncodeTuningModeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_USAGE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_USAGE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeUsageInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'videoUsageHints': ctypes.c_uint32,
    'videoContentHints': ctypes.c_uint32,
    'tuningMode': ctypes.c_int,
}
