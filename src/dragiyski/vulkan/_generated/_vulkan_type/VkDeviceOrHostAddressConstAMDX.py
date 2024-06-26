import ctypes

class VkDeviceOrHostAddressConstAMDX(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDispatchGraphCountInfoAMDX',
        'VkDispatchGraphInfoAMDX',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'deviceAddress': 'device_address',
        'hostAddress': 'host_address',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMDX_shader_enqueue',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceOrHostAddressConstAMDX._type_ = {
    'deviceAddress': ctypes.c_uint64,
    'hostAddress': ctypes.c_void_p,
}
