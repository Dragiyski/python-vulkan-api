import ctypes

class VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxOutputClusterCount', ctypes.c_uint32),
        ('indirectBufferOffsetAlignment', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxWorkGroupCount': 'max_work_group_count',
        'maxWorkGroupSize': 'max_work_group_size',
        'maxOutputClusterCount': 'max_output_cluster_count',
        'indirectBufferOffsetAlignment': 'indirect_buffer_offset_alignment',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_HUAWEI_cluster_culling_shader',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_PROPERTIES_HUAWEI'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_PROPERTIES_HUAWEI
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxWorkGroupCount': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxOutputClusterCount': ctypes.c_uint32,
    'indirectBufferOffsetAlignment': ctypes.c_uint64,
}
