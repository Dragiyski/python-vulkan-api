import ctypes

class VkBufferConstraintsInfoFUCHSIA(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkBufferCollectionConstraintsInfoFUCHSIA',
        'VkBufferCreateInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkSetBufferCollectionBufferConstraintsFUCHSIA',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'createInfo': 'create_info',
        'requiredFormatFeatures': 'required_format_features',
        'bufferCollectionConstraints': 'buffer_collection_constraints',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_FUCHSIA_buffer_collection',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'requiredFormatFeatures': 'VkFormatFeatureFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_CONSTRAINTS_INFO_FUCHSIA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_CONSTRAINTS_INFO_FUCHSIA
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkBufferCollectionConstraintsInfoFUCHSIA import VkBufferCollectionConstraintsInfoFUCHSIA
from .VkBufferCreateInfo import VkBufferCreateInfo

VkBufferConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('createInfo', VkBufferCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
]

VkBufferConstraintsInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'createInfo': VkBufferCreateInfo,
    'requiredFormatFeatures': ctypes.c_uint32,
    'bufferCollectionConstraints': VkBufferCollectionConstraintsInfoFUCHSIA,
}
