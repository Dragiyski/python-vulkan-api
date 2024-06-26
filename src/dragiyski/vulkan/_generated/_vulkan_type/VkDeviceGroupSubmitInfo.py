import ctypes

class VkDeviceGroupSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('commandBufferCount', ctypes.c_uint32),
        ('pCommandBufferDeviceMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('signalSemaphoreCount', ctypes.c_uint32),
        ('pSignalSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkSubmitInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'waitSemaphoreCount': 'wait_semaphore_count',
        'pWaitSemaphoreDeviceIndices': 'wait_semaphore_device_indices',
        'commandBufferCount': 'command_buffer_count',
        'pCommandBufferDeviceMasks': 'command_buffer_device_masks',
        'signalSemaphoreCount': 'signal_semaphore_count',
        'pSignalSemaphoreDeviceIndices': 'signal_semaphore_device_indices',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceGroupSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreCount': ctypes.c_uint32,
    'pWaitSemaphoreDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
    'commandBufferCount': ctypes.c_uint32,
    'pCommandBufferDeviceMasks': ctypes.POINTER(ctypes.c_uint32),
    'signalSemaphoreCount': ctypes.c_uint32,
    'pSignalSemaphoreDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
}
