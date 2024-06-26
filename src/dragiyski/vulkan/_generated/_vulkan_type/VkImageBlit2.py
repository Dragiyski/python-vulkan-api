import ctypes

class VkImageBlit2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkCopyCommandTransformInfoQCOM',
    }
    _includes_ = {
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = {
        'VkBlitImageInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcSubresource': 'src_subresource',
        'srcOffsets': 'src_offsets',
        'dstSubresource': 'dst_subresource',
        'dstOffsets': 'dst_offsets',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_BLIT_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_BLIT_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageBlit2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]

VkImageBlit2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffsets': ctypes.ARRAY(VkOffset3D, 2),
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffsets': ctypes.ARRAY(VkOffset3D, 2),
}
