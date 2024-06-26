import ctypes

class VkPhysicalDeviceTexelBufferAlignmentProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageTexelBufferOffsetAlignmentBytes', ctypes.c_uint64),
        ('storageTexelBufferOffsetSingleTexelAlignment', ctypes.c_uint32),
        ('uniformTexelBufferOffsetAlignmentBytes', ctypes.c_uint64),
        ('uniformTexelBufferOffsetSingleTexelAlignment', ctypes.c_uint32),
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
        'storageTexelBufferOffsetAlignmentBytes': 'storage_texel_buffer_offset_alignment_bytes',
        'storageTexelBufferOffsetSingleTexelAlignment': 'storage_texel_buffer_offset_single_texel_alignment',
        'uniformTexelBufferOffsetAlignmentBytes': 'uniform_texel_buffer_offset_alignment_bytes',
        'uniformTexelBufferOffsetSingleTexelAlignment': 'uniform_texel_buffer_offset_single_texel_alignment',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceTexelBufferAlignmentProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'storageTexelBufferOffsetAlignmentBytes': ctypes.c_uint64,
    'storageTexelBufferOffsetSingleTexelAlignment': ctypes.c_uint32,
    'uniformTexelBufferOffsetAlignmentBytes': ctypes.c_uint64,
    'uniformTexelBufferOffsetSingleTexelAlignment': ctypes.c_uint32,
}
