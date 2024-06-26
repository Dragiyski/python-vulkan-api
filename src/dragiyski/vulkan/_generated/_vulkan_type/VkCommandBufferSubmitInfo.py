import ctypes

class VkCommandBufferSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandBuffer', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkRenderPassStripeSubmitInfoARM',
    }
    _includes_ = set()
    _included_in_ = {
        'VkSubmitInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'commandBuffer': 'command_buffer',
        'deviceMask': 'device_mask',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_SUBMIT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_SUBMIT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkCommandBufferSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'commandBuffer': ctypes.c_void_p,
    'deviceMask': ctypes.c_uint32,
}
