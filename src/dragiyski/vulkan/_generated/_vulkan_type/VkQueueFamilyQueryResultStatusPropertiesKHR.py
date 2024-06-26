import ctypes

class VkQueueFamilyQueryResultStatusPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryResultStatusSupport', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkQueueFamilyProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'queryResultStatusSupport': 'query_result_status_support',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_QUERY_RESULT_STATUS_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_QUERY_RESULT_STATUS_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkQueueFamilyQueryResultStatusPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queryResultStatusSupport': ctypes.c_uint32,
}
