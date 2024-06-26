import ctypes

class VkPipelineCacheHeaderVersionOne(ctypes.Structure):
    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineCacheHeaderVersionSafetyCriticalOne',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'headerSize': 'header_size',
        'headerVersion': 'header_version',
        'vendorID': 'vendor_id',
        'deviceID': 'device_id',
        'pipelineCacheUUID': 'pipeline_cache_uuid',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'headerVersion': 'VkPipelineCacheHeaderVersion',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineCacheHeaderVersionOne._type_ = {
    'headerSize': ctypes.c_uint32,
    'headerVersion': ctypes.c_int,
    'vendorID': ctypes.c_uint32,
    'deviceID': ctypes.c_uint32,
    'pipelineCacheUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
}
