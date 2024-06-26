import ctypes

class VkAndroidHardwareBufferFormatResolvePropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentFormat', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkAndroidHardwareBufferPropertiesANDROID',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'colorAttachmentFormat': 'color_attachment_format',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ANDROID_external_format_resolve',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'colorAttachmentFormat': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_RESOLVE_PROPERTIES_ANDROID'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_RESOLVE_PROPERTIES_ANDROID
        for function in self._init_:
            function(self, *args, **kwargs)

VkAndroidHardwareBufferFormatResolvePropertiesANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'colorAttachmentFormat': ctypes.c_int,
}
