import ctypes

class VkPipelineExecutableInternalRepresentationKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('isText', ctypes.c_uint32),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPipelineExecutableInternalRepresentationsKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'name': 'name',
        'description': 'description',
        'isText': 'is_text',
        'dataSize': 'data_size',
        'pData': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_pipeline_executable_properties',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineExecutableInternalRepresentationKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'name': ctypes.ARRAY(ctypes.c_char, 256),
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'isText': ctypes.c_uint32,
    'dataSize': ctypes.c_size_t,
    'pData': ctypes.c_void_p,
}
