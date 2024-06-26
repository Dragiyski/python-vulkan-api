import ctypes

class VkSpecializationInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkSpecializationMapEntry',
    }
    _included_in_ = {
        'VkPipelineShaderStageCreateInfo',
        'VkShaderCreateInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'mapEntryCount': 'map_entry_count',
        'pMapEntries': 'map_entries',
        'dataSize': 'data_size',
        'pData': 'data',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSpecializationMapEntry import VkSpecializationMapEntry

VkSpecializationInfo._fields_ = [
    ('mapEntryCount', ctypes.c_uint32),
    ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)),
    ('dataSize', ctypes.c_size_t),
    ('pData', ctypes.c_void_p),
]

VkSpecializationInfo._type_ = {
    'mapEntryCount': ctypes.c_uint32,
    'pMapEntries': ctypes.POINTER(VkSpecializationMapEntry),
    'dataSize': ctypes.c_size_t,
    'pData': ctypes.c_void_p,
}
