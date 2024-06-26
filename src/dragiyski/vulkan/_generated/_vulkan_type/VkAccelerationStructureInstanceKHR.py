import ctypes

class VkAccelerationStructureInstanceKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkTransformMatrixKHR',
    }
    _included_in_ = {
        'VkAccelerationStructureMotionInstanceDataNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'transform': 'transform',
        'instanceCustomIndex': 'instance_custom_index',
        'mask': 'mask',
        'instanceShaderBindingTableRecordOffset': 'instance_shader_binding_table_record_offset',
        'flags': 'flags',
        'accelerationStructureReference': 'acceleration_structure_reference',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'flags': 'VkGeometryInstanceFlagsKHR',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkTransformMatrixKHR import VkTransformMatrixKHR

VkAccelerationStructureInstanceKHR._fields_ = [
    ('transform', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]

VkAccelerationStructureInstanceKHR._type_ = {
    'transform': VkTransformMatrixKHR,
    'instanceCustomIndex': ctypes.c_uint32,
    'mask': ctypes.c_uint32,
    'instanceShaderBindingTableRecordOffset': ctypes.c_uint32,
    'flags': ctypes.c_uint32,
    'accelerationStructureReference': ctypes.c_uint64,
}
