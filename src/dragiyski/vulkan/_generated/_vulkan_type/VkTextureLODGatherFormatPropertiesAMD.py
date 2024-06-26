import ctypes

class VkTextureLODGatherFormatPropertiesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportsTextureGatherLODBiasAMD', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkImageFormatProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'supportsTextureGatherLODBiasAMD': 'supports_texture_gather_lodbias_amd',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_texture_gather_bias_lod',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_TEXTURE_LOD_GATHER_FORMAT_PROPERTIES_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_TEXTURE_LOD_GATHER_FORMAT_PROPERTIES_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkTextureLODGatherFormatPropertiesAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportsTextureGatherLODBiasAMD': ctypes.c_uint32,
}
