import ctypes

class VkDispatchGraphInfoAMDX(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstAMDX',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'nodeIndex': 'node_index',
        'payloadCount': 'payload_count',
        'payloads': 'payloads',
        'payloadStride': 'payload_stride',
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

VkDispatchGraphInfoAMDX._fields_ = [
    ('nodeIndex', ctypes.c_uint32),
    ('payloadCount', ctypes.c_uint32),
    ('payloads', VkDeviceOrHostAddressConstAMDX),
    ('payloadStride', ctypes.c_uint64),
]

VkDispatchGraphInfoAMDX._type_ = {
    'nodeIndex': ctypes.c_uint32,
    'payloadCount': ctypes.c_uint32,
    'payloads': VkDeviceOrHostAddressConstAMDX,
    'payloadStride': ctypes.c_uint64,
}
