import ctypes

class VkSemaphoreSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
        ('stageMask', ctypes.c_uint64),
        ('deviceIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassStripeSubmitInfoARM',
        'VkSubmitInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'semaphore': 'semaphore',
        'value': 'value',
        'stageMask': 'stage_mask',
        'deviceIndex': 'device_index',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stageMask': 'VkPipelineStageFlags2',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SEMAPHORE_SUBMIT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_SUBMIT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSemaphoreSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphore': ctypes.c_void_p,
    'value': ctypes.c_uint64,
    'stageMask': ctypes.c_uint64,
    'deviceIndex': ctypes.c_uint32,
}
