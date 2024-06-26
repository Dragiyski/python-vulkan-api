import ctypes

class VkPhysicalDeviceHostImageCopyPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('copySrcLayoutCount', ctypes.c_uint32),
        ('pCopySrcLayouts', ctypes.POINTER(ctypes.c_int)),
        ('copyDstLayoutCount', ctypes.c_uint32),
        ('pCopyDstLayouts', ctypes.POINTER(ctypes.c_int)),
        ('optimalTilingLayoutUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('identicalMemoryTypeRequirements', ctypes.c_uint32),
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
        'copySrcLayoutCount': 'copy_src_layout_count',
        'pCopySrcLayouts': 'copy_src_layouts',
        'copyDstLayoutCount': 'copy_dst_layout_count',
        'pCopyDstLayouts': 'copy_dst_layouts',
        'optimalTilingLayoutUUID': 'optimal_tiling_layout_uuid',
        'identicalMemoryTypeRequirements': 'identical_memory_type_requirements',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_host_image_copy',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pCopySrcLayouts': 'VkImageLayout',
        'pCopyDstLayouts': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_IMAGE_COPY_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_IMAGE_COPY_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceHostImageCopyPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'copySrcLayoutCount': ctypes.c_uint32,
    'pCopySrcLayouts': ctypes.POINTER(ctypes.c_int),
    'copyDstLayoutCount': ctypes.c_uint32,
    'pCopyDstLayouts': ctypes.POINTER(ctypes.c_int),
    'optimalTilingLayoutUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'identicalMemoryTypeRequirements': ctypes.c_uint32,
}
