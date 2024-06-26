import ctypes

class VkPhysicalDeviceMeshShaderPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxDrawMeshTasksCount', ctypes.c_uint32),
        ('maxTaskWorkGroupInvocations', ctypes.c_uint32),
        ('maxTaskWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxTaskTotalMemorySize', ctypes.c_uint32),
        ('maxTaskOutputCount', ctypes.c_uint32),
        ('maxMeshWorkGroupInvocations', ctypes.c_uint32),
        ('maxMeshWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxMeshTotalMemorySize', ctypes.c_uint32),
        ('maxMeshOutputVertices', ctypes.c_uint32),
        ('maxMeshOutputPrimitives', ctypes.c_uint32),
        ('maxMeshMultiviewViewCount', ctypes.c_uint32),
        ('meshOutputPerVertexGranularity', ctypes.c_uint32),
        ('meshOutputPerPrimitiveGranularity', ctypes.c_uint32),
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
        'maxDrawMeshTasksCount': 'max_draw_mesh_tasks_count',
        'maxTaskWorkGroupInvocations': 'max_task_work_group_invocations',
        'maxTaskWorkGroupSize': 'max_task_work_group_size',
        'maxTaskTotalMemorySize': 'max_task_total_memory_size',
        'maxTaskOutputCount': 'max_task_output_count',
        'maxMeshWorkGroupInvocations': 'max_mesh_work_group_invocations',
        'maxMeshWorkGroupSize': 'max_mesh_work_group_size',
        'maxMeshTotalMemorySize': 'max_mesh_total_memory_size',
        'maxMeshOutputVertices': 'max_mesh_output_vertices',
        'maxMeshOutputPrimitives': 'max_mesh_output_primitives',
        'maxMeshMultiviewViewCount': 'max_mesh_multiview_view_count',
        'meshOutputPerVertexGranularity': 'mesh_output_per_vertex_granularity',
        'meshOutputPerPrimitiveGranularity': 'mesh_output_per_primitive_granularity',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_mesh_shader',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceMeshShaderPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxDrawMeshTasksCount': ctypes.c_uint32,
    'maxTaskWorkGroupInvocations': ctypes.c_uint32,
    'maxTaskWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxTaskTotalMemorySize': ctypes.c_uint32,
    'maxTaskOutputCount': ctypes.c_uint32,
    'maxMeshWorkGroupInvocations': ctypes.c_uint32,
    'maxMeshWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxMeshTotalMemorySize': ctypes.c_uint32,
    'maxMeshOutputVertices': ctypes.c_uint32,
    'maxMeshOutputPrimitives': ctypes.c_uint32,
    'maxMeshMultiviewViewCount': ctypes.c_uint32,
    'meshOutputPerVertexGranularity': ctypes.c_uint32,
    'meshOutputPerPrimitiveGranularity': ctypes.c_uint32,
}
