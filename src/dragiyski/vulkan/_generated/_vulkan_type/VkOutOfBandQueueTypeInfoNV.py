import ctypes

class VkOutOfBandQueueTypeInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queueType', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkQueueNotifyOutOfBandNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'queueType': 'queue_type',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_low_latency2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'queueType': 'VkOutOfBandQueueTypeNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_OUT_OF_BAND_QUEUE_TYPE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_OUT_OF_BAND_QUEUE_TYPE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkOutOfBandQueueTypeInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queueType': ctypes.c_int,
}
