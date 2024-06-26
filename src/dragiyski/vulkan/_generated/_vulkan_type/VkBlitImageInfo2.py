import ctypes

class VkBlitImageInfo2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkBlitImageCubicWeightsInfoQCOM',
    }
    _includes_ = {
        'VkImageBlit2',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBlitImage2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcImage': 'src_image',
        'srcImageLayout': 'src_image_layout',
        'dstImage': 'dst_image',
        'dstImageLayout': 'dst_image_layout',
        'regionCount': 'region_count',
        'pRegions': 'regions',
        'filter': 'filter',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'srcImageLayout': 'VkImageLayout',
        'dstImageLayout': 'VkImageLayout',
        'filter': 'VkFilter',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BLIT_IMAGE_INFO_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BLIT_IMAGE_INFO_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageBlit2 import VkImageBlit2

VkBlitImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageBlit2)),
    ('filter', ctypes.c_int),
]

VkBlitImageInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcImage': ctypes.c_void_p,
    'srcImageLayout': ctypes.c_int,
    'dstImage': ctypes.c_void_p,
    'dstImageLayout': ctypes.c_int,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkImageBlit2),
    'filter': ctypes.c_int,
}
