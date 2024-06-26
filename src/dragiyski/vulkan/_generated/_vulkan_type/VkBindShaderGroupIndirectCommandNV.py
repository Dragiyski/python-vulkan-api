import ctypes

class VkBindShaderGroupIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('groupIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'groupIndex': 'group_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkBindShaderGroupIndirectCommandNV._type_ = {
    'groupIndex': ctypes.c_uint32,
}
