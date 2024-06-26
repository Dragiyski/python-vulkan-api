import ctypes

class VkQueueFamilyProperties(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
    }
    _included_in_ = {
        'VkQueueFamilyProperties2',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceQueueFamilyProperties',
    }
    _python_name_ = {
        'queueFlags': 'queue_flags',
        'queueCount': 'queue_count',
        'timestampValidBits': 'timestamp_valid_bits',
        'minImageTransferGranularity': 'min_image_transfer_granularity',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'queueFlags': 'VkQueueFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D

VkQueueFamilyProperties._fields_ = [
    ('queueFlags', ctypes.c_uint32),
    ('queueCount', ctypes.c_uint32),
    ('timestampValidBits', ctypes.c_uint32),
    ('minImageTransferGranularity', VkExtent3D),
]

VkQueueFamilyProperties._type_ = {
    'queueFlags': ctypes.c_uint32,
    'queueCount': ctypes.c_uint32,
    'timestampValidBits': ctypes.c_uint32,
    'minImageTransferGranularity': VkExtent3D,
}
