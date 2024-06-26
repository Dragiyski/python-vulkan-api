import ctypes

class VkPhysicalDeviceShaderTileImagePropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTileImageCoherentReadAccelerated', ctypes.c_uint32),
        ('shaderTileImageReadSampleFromPixelRateInvocation', ctypes.c_uint32),
        ('shaderTileImageReadFromHelperInvocation', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shaderTileImageCoherentReadAccelerated': 'shader_tile_image_coherent_read_accelerated',
        'shaderTileImageReadSampleFromPixelRateInvocation': 'shader_tile_image_read_sample_from_pixel_rate_invocation',
        'shaderTileImageReadFromHelperInvocation': 'shader_tile_image_read_from_helper_invocation',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_shader_tile_image',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderTileImagePropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderTileImageCoherentReadAccelerated': ctypes.c_uint32,
    'shaderTileImageReadSampleFromPixelRateInvocation': ctypes.c_uint32,
    'shaderTileImageReadFromHelperInvocation': ctypes.c_uint32,
}
