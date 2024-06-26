import ctypes

class VkPhysicalDeviceExternalFormatResolvePropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nullColorAttachmentWithExternalFormatResolve', ctypes.c_uint32),
        ('externalFormatResolveChromaOffsetX', ctypes.c_int),
        ('externalFormatResolveChromaOffsetY', ctypes.c_int),
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
        'nullColorAttachmentWithExternalFormatResolve': 'null_color_attachment_with_external_format_resolve',
        'externalFormatResolveChromaOffsetX': 'external_format_resolve_chroma_offset_x',
        'externalFormatResolveChromaOffsetY': 'external_format_resolve_chroma_offset_y',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ANDROID_external_format_resolve',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'externalFormatResolveChromaOffsetX': 'VkChromaLocation',
        'externalFormatResolveChromaOffsetY': 'VkChromaLocation',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FORMAT_RESOLVE_PROPERTIES_ANDROID'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FORMAT_RESOLVE_PROPERTIES_ANDROID
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceExternalFormatResolvePropertiesANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'nullColorAttachmentWithExternalFormatResolve': ctypes.c_uint32,
    'externalFormatResolveChromaOffsetX': ctypes.c_int,
    'externalFormatResolveChromaOffsetY': ctypes.c_int,
}
