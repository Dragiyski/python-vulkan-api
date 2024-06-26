import ctypes

class VkRenderPassSampleLocationsBeginInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkRenderPassBeginInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkAttachmentSampleLocationsEXT',
        'VkSubpassSampleLocationsEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'attachmentInitialSampleLocationsCount': 'attachment_initial_sample_locations_count',
        'pAttachmentInitialSampleLocations': 'attachment_initial_sample_locations',
        'postSubpassSampleLocationsCount': 'post_subpass_sample_locations_count',
        'pPostSubpassSampleLocations': 'post_subpass_sample_locations',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_sample_locations',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAttachmentSampleLocationsEXT import VkAttachmentSampleLocationsEXT
from .VkSubpassSampleLocationsEXT import VkSubpassSampleLocationsEXT

VkRenderPassSampleLocationsBeginInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentInitialSampleLocationsCount', ctypes.c_uint32),
    ('pAttachmentInitialSampleLocations', ctypes.POINTER(VkAttachmentSampleLocationsEXT)),
    ('postSubpassSampleLocationsCount', ctypes.c_uint32),
    ('pPostSubpassSampleLocations', ctypes.POINTER(VkSubpassSampleLocationsEXT)),
]

VkRenderPassSampleLocationsBeginInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentInitialSampleLocationsCount': ctypes.c_uint32,
    'pAttachmentInitialSampleLocations': ctypes.POINTER(VkAttachmentSampleLocationsEXT),
    'postSubpassSampleLocationsCount': ctypes.c_uint32,
    'pPostSubpassSampleLocations': ctypes.POINTER(VkSubpassSampleLocationsEXT),
}
