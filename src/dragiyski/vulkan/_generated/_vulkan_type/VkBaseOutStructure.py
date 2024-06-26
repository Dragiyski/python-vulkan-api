import ctypes

class VkBaseOutStructure(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkBaseOutStructure',
    }
    _included_in_ = {
        'VkBaseOutStructure',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPipelinePropertiesEXT',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)



VkBaseOutStructure._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseOutStructure)),
]

VkBaseOutStructure._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.POINTER(VkBaseOutStructure),
}
