import ctypes

class VkTraceRaysIndirectCommand2KHR(ctypes.Structure):
    _fields_ = [
        ('raygenShaderRecordAddress', ctypes.c_uint64),
        ('raygenShaderRecordSize', ctypes.c_uint64),
        ('missShaderBindingTableAddress', ctypes.c_uint64),
        ('missShaderBindingTableSize', ctypes.c_uint64),
        ('missShaderBindingTableStride', ctypes.c_uint64),
        ('hitShaderBindingTableAddress', ctypes.c_uint64),
        ('hitShaderBindingTableSize', ctypes.c_uint64),
        ('hitShaderBindingTableStride', ctypes.c_uint64),
        ('callableShaderBindingTableAddress', ctypes.c_uint64),
        ('callableShaderBindingTableSize', ctypes.c_uint64),
        ('callableShaderBindingTableStride', ctypes.c_uint64),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'raygenShaderRecordAddress': 'raygen_shader_record_address',
        'raygenShaderRecordSize': 'raygen_shader_record_size',
        'missShaderBindingTableAddress': 'miss_shader_binding_table_address',
        'missShaderBindingTableSize': 'miss_shader_binding_table_size',
        'missShaderBindingTableStride': 'miss_shader_binding_table_stride',
        'hitShaderBindingTableAddress': 'hit_shader_binding_table_address',
        'hitShaderBindingTableSize': 'hit_shader_binding_table_size',
        'hitShaderBindingTableStride': 'hit_shader_binding_table_stride',
        'callableShaderBindingTableAddress': 'callable_shader_binding_table_address',
        'callableShaderBindingTableSize': 'callable_shader_binding_table_size',
        'callableShaderBindingTableStride': 'callable_shader_binding_table_stride',
        'width': 'width',
        'height': 'height',
        'depth': 'depth',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_maintenance1',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkTraceRaysIndirectCommand2KHR._type_ = {
    'raygenShaderRecordAddress': ctypes.c_uint64,
    'raygenShaderRecordSize': ctypes.c_uint64,
    'missShaderBindingTableAddress': ctypes.c_uint64,
    'missShaderBindingTableSize': ctypes.c_uint64,
    'missShaderBindingTableStride': ctypes.c_uint64,
    'hitShaderBindingTableAddress': ctypes.c_uint64,
    'hitShaderBindingTableSize': ctypes.c_uint64,
    'hitShaderBindingTableStride': ctypes.c_uint64,
    'callableShaderBindingTableAddress': ctypes.c_uint64,
    'callableShaderBindingTableSize': ctypes.c_uint64,
    'callableShaderBindingTableStride': ctypes.c_uint64,
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'depth': ctypes.c_uint32,
}
