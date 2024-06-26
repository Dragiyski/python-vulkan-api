import ctypes

class VkAccelerationStructureSRTMotionInstanceNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkSRTDataNV',
    }
    _included_in_ = {
        'VkAccelerationStructureMotionInstanceDataNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'transformT0': 'transform_t0',
        'transformT1': 'transform_t1',
        'instanceCustomIndex': 'instance_custom_index',
        'mask': 'mask',
        'instanceShaderBindingTableRecordOffset': 'instance_shader_binding_table_record_offset',
        'flags': 'flags',
        'accelerationStructureReference': 'acceleration_structure_reference',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_motion_blur',
    }
    _vk_enum_ = {
        'flags': 'VkGeometryInstanceFlagsKHR',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSRTDataNV import VkSRTDataNV

VkAccelerationStructureSRTMotionInstanceNV._fields_ = [
    ('transformT0', VkSRTDataNV),
    ('transformT1', VkSRTDataNV),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]

VkAccelerationStructureSRTMotionInstanceNV._type_ = {
    'transformT0': VkSRTDataNV,
    'transformT1': VkSRTDataNV,
    'instanceCustomIndex': ctypes.c_uint32,
    'mask': ctypes.c_uint32,
    'instanceShaderBindingTableRecordOffset': ctypes.c_uint32,
    'flags': ctypes.c_uint32,
    'accelerationStructureReference': ctypes.c_uint64,
}
