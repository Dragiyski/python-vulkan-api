import ctypes

class VkMultiDrawInfoEXT(ctypes.Structure):
    _fields_ = [
        ('firstVertex', ctypes.c_uint32),
        ('vertexCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdDrawMultiEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'firstVertex': 'first_vertex',
        'vertexCount': 'vertex_count',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_multi_draw',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkMultiDrawInfoEXT._type_ = {
    'firstVertex': ctypes.c_uint32,
    'vertexCount': ctypes.c_uint32,
}
