import ctypes

class VkMultiDrawIndexedInfoEXT(ctypes.Structure):
    _fields_ = [
        ('firstIndex', ctypes.c_uint32),
        ('indexCount', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdDrawMultiIndexedEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'firstIndex': 'first_index',
        'indexCount': 'index_count',
        'vertexOffset': 'vertex_offset',
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

VkMultiDrawIndexedInfoEXT._type_ = {
    'firstIndex': ctypes.c_uint32,
    'indexCount': ctypes.c_uint32,
    'vertexOffset': ctypes.c_int32,
}
