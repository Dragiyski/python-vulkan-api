import ctypes

class VkVideoEncodeRateControlInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoBeginCodingInfoKHR',
        'VkVideoCodingControlInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVideoEncodeRateControlLayerInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'rateControlMode': 'rate_control_mode',
        'layerCount': 'layer_count',
        'pLayers': 'layers',
        'virtualBufferSizeInMs': 'virtual_buffer_size_in_ms',
        'initialVirtualBufferSizeInMs': 'initial_virtual_buffer_size_in_ms',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoEncodeRateControlFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoEncodeRateControlLayerInfoKHR import VkVideoEncodeRateControlLayerInfoKHR

VkVideoEncodeRateControlInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlMode', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
    ('pLayers', ctypes.POINTER(VkVideoEncodeRateControlLayerInfoKHR)),
    ('virtualBufferSizeInMs', ctypes.c_uint32),
    ('initialVirtualBufferSizeInMs', ctypes.c_uint32),
]

VkVideoEncodeRateControlInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'rateControlMode': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
    'pLayers': ctypes.POINTER(VkVideoEncodeRateControlLayerInfoKHR),
    'virtualBufferSizeInMs': ctypes.c_uint32,
    'initialVirtualBufferSizeInMs': ctypes.c_uint32,
}
