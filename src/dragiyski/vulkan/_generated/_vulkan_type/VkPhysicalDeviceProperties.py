import ctypes

class VkPhysicalDeviceProperties(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkPhysicalDeviceLimits',
        'VkPhysicalDeviceSparseProperties',
    }
    _included_in_ = {
        'VkPhysicalDeviceProperties2',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceProperties',
    }
    _python_name_ = {
        'apiVersion': 'api_version',
        'driverVersion': 'driver_version',
        'vendorID': 'vendor_id',
        'deviceID': 'device_id',
        'deviceType': 'device_type',
        'deviceName': 'device_name',
        'pipelineCacheUUID': 'pipeline_cache_uuid',
        'limits': 'limits',
        'sparseProperties': 'sparse_properties',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'deviceType': 'VkPhysicalDeviceType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPhysicalDeviceLimits import VkPhysicalDeviceLimits
from .VkPhysicalDeviceSparseProperties import VkPhysicalDeviceSparseProperties

VkPhysicalDeviceProperties._fields_ = [
    ('apiVersion', ctypes.c_uint32),
    ('driverVersion', ctypes.c_uint32),
    ('vendorID', ctypes.c_uint32),
    ('deviceID', ctypes.c_uint32),
    ('deviceType', ctypes.c_int),
    ('deviceName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ('limits', VkPhysicalDeviceLimits),
    ('sparseProperties', VkPhysicalDeviceSparseProperties),
]

VkPhysicalDeviceProperties._type_ = {
    'apiVersion': ctypes.c_uint32,
    'driverVersion': ctypes.c_uint32,
    'vendorID': ctypes.c_uint32,
    'deviceID': ctypes.c_uint32,
    'deviceType': ctypes.c_int,
    'deviceName': ctypes.ARRAY(ctypes.c_char, 256),
    'pipelineCacheUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'limits': VkPhysicalDeviceLimits,
    'sparseProperties': VkPhysicalDeviceSparseProperties,
}
