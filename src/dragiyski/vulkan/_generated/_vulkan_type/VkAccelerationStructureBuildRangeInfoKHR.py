import ctypes

class VkAccelerationStructureBuildRangeInfoKHR(ctypes.Structure):
    _fields_ = [
        ('primitiveCount', ctypes.c_uint32),
        ('primitiveOffset', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('transformOffset', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkBuildAccelerationStructuresKHR',
        'vkCmdBuildAccelerationStructuresKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'primitiveCount': 'primitive_count',
        'primitiveOffset': 'primitive_offset',
        'firstVertex': 'first_vertex',
        'transformOffset': 'transform_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkAccelerationStructureBuildRangeInfoKHR._type_ = {
    'primitiveCount': ctypes.c_uint32,
    'primitiveOffset': ctypes.c_uint32,
    'firstVertex': ctypes.c_uint32,
    'transformOffset': ctypes.c_uint32,
}
