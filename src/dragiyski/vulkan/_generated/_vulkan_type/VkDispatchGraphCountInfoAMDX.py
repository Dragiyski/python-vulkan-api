import ctypes

class VkDispatchGraphCountInfoAMDX(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstAMDX',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdDispatchGraphAMDX',
        'vkCmdDispatchGraphIndirectAMDX',
    }
    _output_of_ = set()
    _python_name_ = {
        'count': 'count',
        'infos': 'infos',
        'stride': 'stride',
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


from .VkDeviceOrHostAddressConstAMDX import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphCountInfoAMDX._fields_ = [
    ('count', ctypes.c_uint32),
    ('infos', VkDeviceOrHostAddressConstAMDX),
    ('stride', ctypes.c_uint64),
]

VkDispatchGraphCountInfoAMDX._type_ = {
    'count': ctypes.c_uint32,
    'infos': VkDeviceOrHostAddressConstAMDX,
    'stride': ctypes.c_uint64,
}
