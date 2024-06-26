import ctypes

class VkImageResolve(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdResolveImage',
    }
    _output_of_ = set()
    _python_name_ = {
        'srcSubresource': 'src_subresource',
        'srcOffset': 'src_offset',
        'dstSubresource': 'dst_subresource',
        'dstOffset': 'dst_offset',
        'extent': 'extent',
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


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageResolve._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]

VkImageResolve._type_ = {
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffset': VkOffset3D,
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffset': VkOffset3D,
    'extent': VkExtent3D,
}
