import ctypes

class VkExportMetalTextureInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('bufferView', ctypes.c_void_p),
        ('plane', ctypes.c_uint32),
        ('mtlTexture', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = {
        'VkExportMetalObjectsInfoEXT',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'image': 'image',
        'imageView': 'image_view',
        'bufferView': 'buffer_view',
        'plane': 'plane',
        'mtlTexture': 'mtl_texture',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_metal_objects',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXPORT_METAL_TEXTURE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_TEXTURE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkExportMetalTextureInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'image': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'bufferView': ctypes.c_void_p,
    'plane': ctypes.c_uint32,
    'mtlTexture': ctypes.c_void_p,
}
