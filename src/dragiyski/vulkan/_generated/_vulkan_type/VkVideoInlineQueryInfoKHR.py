import ctypes

class VkVideoInlineQueryInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryPool', ctypes.c_void_p),
        ('firstQuery', ctypes.c_uint32),
        ('queryCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkVideoDecodeInfoKHR',
        'VkVideoEncodeInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'queryPool': 'query_pool',
        'firstQuery': 'first_query',
        'queryCount': 'query_count',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_maintenance1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_INLINE_QUERY_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_INLINE_QUERY_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoInlineQueryInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queryPool': ctypes.c_void_p,
    'firstQuery': ctypes.c_uint32,
    'queryCount': ctypes.c_uint32,
}
