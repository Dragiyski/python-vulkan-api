import ctypes

class VkStridedDeviceAddressRegionKHR(ctypes.Structure):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('stride', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdTraceRaysIndirectKHR',
        'vkCmdTraceRaysKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'deviceAddress': 'device_address',
        'stride': 'stride',
        'size': 'size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_pipeline',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkStridedDeviceAddressRegionKHR._type_ = {
    'deviceAddress': ctypes.c_uint64,
    'stride': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
