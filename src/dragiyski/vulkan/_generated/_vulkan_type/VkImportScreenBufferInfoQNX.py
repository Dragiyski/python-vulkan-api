import ctypes

class VkImportScreenBufferInfoQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = {
        'VkMemoryAllocateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'buffer': 'buffer',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QNX_external_memory_screen_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMPORT_SCREEN_BUFFER_INFO_QNX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SCREEN_BUFFER_INFO_QNX
        for function in self._init_:
            function(self, *args, **kwargs)

VkImportScreenBufferInfoQNX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'buffer': ctypes.c_void_p,
}
