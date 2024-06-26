import ctypes

class VkImageViewASTCDecodeModeEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('decodeMode', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkImageViewCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'decodeMode': 'decode_mode',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_astc_decode_mode',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'decodeMode': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_VIEW_ASTC_DECODE_MODE_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_ASTC_DECODE_MODE_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageViewASTCDecodeModeEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'decodeMode': ctypes.c_int,
}
