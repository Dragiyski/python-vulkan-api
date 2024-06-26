import ctypes

class VkCheckpointDataNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint32),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetQueueCheckpointDataNV',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stage': 'stage',
        'pCheckpointMarker': 'checkpoint_marker',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_diagnostic_checkpoints',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_CHECKPOINT_DATA_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_CHECKPOINT_DATA_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkCheckpointDataNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stage': ctypes.c_uint32,
    'pCheckpointMarker': ctypes.c_void_p,
}
