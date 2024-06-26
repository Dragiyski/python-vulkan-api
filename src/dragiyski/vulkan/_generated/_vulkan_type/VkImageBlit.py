import ctypes

class VkImageBlit(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBlitImage',
    }
    _output_of_ = set()
    _python_name_ = {
        'srcSubresource': 'src_subresource',
        'srcOffsets': 'src_offsets',
        'dstSubresource': 'dst_subresource',
        'dstOffsets': 'dst_offsets',
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


from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageBlit._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]

VkImageBlit._type_ = {
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffsets': ctypes.ARRAY(VkOffset3D, 2),
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffsets': ctypes.ARRAY(VkOffset3D, 2),
}
