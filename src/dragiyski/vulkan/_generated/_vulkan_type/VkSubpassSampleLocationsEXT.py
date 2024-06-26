import ctypes

class VkSubpassSampleLocationsEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkSampleLocationsInfoEXT',
    }
    _included_in_ = {
        'VkRenderPassSampleLocationsBeginInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'subpassIndex': 'subpass_index',
        'sampleLocationsInfo': 'sample_locations_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_sample_locations',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkSubpassSampleLocationsEXT._fields_ = [
    ('subpassIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

VkSubpassSampleLocationsEXT._type_ = {
    'subpassIndex': ctypes.c_uint32,
    'sampleLocationsInfo': VkSampleLocationsInfoEXT,
}
