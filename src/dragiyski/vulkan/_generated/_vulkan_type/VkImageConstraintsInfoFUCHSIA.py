import ctypes

class VkImageConstraintsInfoFUCHSIA(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkBufferCollectionConstraintsInfoFUCHSIA',
        'VkImageFormatConstraintsInfoFUCHSIA',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkSetBufferCollectionImageConstraintsFUCHSIA',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'formatConstraintsCount': 'format_constraints_count',
        'pFormatConstraints': 'format_constraints',
        'bufferCollectionConstraints': 'buffer_collection_constraints',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_FUCHSIA_buffer_collection',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkImageConstraintsInfoFlagsFUCHSIA',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_CONSTRAINTS_INFO_FUCHSIA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_CONSTRAINTS_INFO_FUCHSIA
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkBufferCollectionConstraintsInfoFUCHSIA import VkBufferCollectionConstraintsInfoFUCHSIA
from .VkImageFormatConstraintsInfoFUCHSIA import VkImageFormatConstraintsInfoFUCHSIA

VkImageConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatConstraintsCount', ctypes.c_uint32),
    ('pFormatConstraints', ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA)),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
    ('flags', ctypes.c_uint32),
]

VkImageConstraintsInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'formatConstraintsCount': ctypes.c_uint32,
    'pFormatConstraints': ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA),
    'bufferCollectionConstraints': VkBufferCollectionConstraintsInfoFUCHSIA,
    'flags': ctypes.c_uint32,
}
