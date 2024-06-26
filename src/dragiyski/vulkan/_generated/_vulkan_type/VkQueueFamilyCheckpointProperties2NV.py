import ctypes

class VkQueueFamilyCheckpointProperties2NV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('checkpointExecutionStageMask', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkQueueFamilyProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'checkpointExecutionStageMask': 'checkpoint_execution_stage_mask',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_synchronization2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'checkpointExecutionStageMask': 'VkPipelineStageFlags2',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_2_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_2_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkQueueFamilyCheckpointProperties2NV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'checkpointExecutionStageMask': ctypes.c_uint64,
}
