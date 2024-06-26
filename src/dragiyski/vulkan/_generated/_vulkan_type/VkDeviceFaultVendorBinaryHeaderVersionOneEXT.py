import ctypes

class VkDeviceFaultVendorBinaryHeaderVersionOneEXT(ctypes.Structure):
    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('driverVersion', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('applicationNameOffset', ctypes.c_uint32),
        ('applicationVersion', ctypes.c_uint32),
        ('engineNameOffset', ctypes.c_uint32),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'headerSize': 'header_size',
        'headerVersion': 'header_version',
        'vendorID': 'vendor_id',
        'deviceID': 'device_id',
        'driverVersion': 'driver_version',
        'pipelineCacheUUID': 'pipeline_cache_uuid',
        'applicationNameOffset': 'application_name_offset',
        'applicationVersion': 'application_version',
        'engineNameOffset': 'engine_name_offset',
        'engineVersion': 'engine_version',
        'apiVersion': 'api_version',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_fault',
    }
    _vk_enum_ = {
        'headerVersion': 'VkDeviceFaultVendorBinaryHeaderVersionEXT',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceFaultVendorBinaryHeaderVersionOneEXT._type_ = {
    'headerSize': ctypes.c_uint32,
    'headerVersion': ctypes.c_int,
    'vendorID': ctypes.c_uint32,
    'deviceID': ctypes.c_uint32,
    'driverVersion': ctypes.c_uint32,
    'pipelineCacheUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'applicationNameOffset': ctypes.c_uint32,
    'applicationVersion': ctypes.c_uint32,
    'engineNameOffset': ctypes.c_uint32,
    'engineVersion': ctypes.c_uint32,
    'apiVersion': ctypes.c_uint32,
}
