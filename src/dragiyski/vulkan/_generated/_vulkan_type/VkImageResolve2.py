import ctypes

class VkImageResolve2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = {
        'VkResolveImageInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcSubresource': 'src_subresource',
        'srcOffset': 'src_offset',
        'dstSubresource': 'dst_subresource',
        'dstOffset': 'dst_offset',
        'extent': 'extent',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_RESOLVE_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_RESOLVE_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageResolve2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]

VkImageResolve2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffset': VkOffset3D,
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffset': VkOffset3D,
    'extent': VkExtent3D,
}
