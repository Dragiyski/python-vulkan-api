import ctypes

class VkPhysicalDeviceMeshShaderPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxTaskWorkGroupTotalCount', ctypes.c_uint32),
        ('maxTaskWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxTaskWorkGroupInvocations', ctypes.c_uint32),
        ('maxTaskWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxTaskPayloadSize', ctypes.c_uint32),
        ('maxTaskSharedMemorySize', ctypes.c_uint32),
        ('maxTaskPayloadAndSharedMemorySize', ctypes.c_uint32),
        ('maxMeshWorkGroupTotalCount', ctypes.c_uint32),
        ('maxMeshWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxMeshWorkGroupInvocations', ctypes.c_uint32),
        ('maxMeshWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxMeshSharedMemorySize', ctypes.c_uint32),
        ('maxMeshPayloadAndSharedMemorySize', ctypes.c_uint32),
        ('maxMeshOutputMemorySize', ctypes.c_uint32),
        ('maxMeshPayloadAndOutputMemorySize', ctypes.c_uint32),
        ('maxMeshOutputComponents', ctypes.c_uint32),
        ('maxMeshOutputVertices', ctypes.c_uint32),
        ('maxMeshOutputPrimitives', ctypes.c_uint32),
        ('maxMeshOutputLayers', ctypes.c_uint32),
        ('maxMeshMultiviewViewCount', ctypes.c_uint32),
        ('meshOutputPerVertexGranularity', ctypes.c_uint32),
        ('meshOutputPerPrimitiveGranularity', ctypes.c_uint32),
        ('maxPreferredTaskWorkGroupInvocations', ctypes.c_uint32),
        ('maxPreferredMeshWorkGroupInvocations', ctypes.c_uint32),
        ('prefersLocalInvocationVertexOutput', ctypes.c_uint32),
        ('prefersLocalInvocationPrimitiveOutput', ctypes.c_uint32),
        ('prefersCompactVertexOutput', ctypes.c_uint32),
        ('prefersCompactPrimitiveOutput', ctypes.c_uint32),
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
        'maxTaskWorkGroupTotalCount': 'max_task_work_group_total_count',
        'maxTaskWorkGroupCount': 'max_task_work_group_count',
        'maxTaskWorkGroupInvocations': 'max_task_work_group_invocations',
        'maxTaskWorkGroupSize': 'max_task_work_group_size',
        'maxTaskPayloadSize': 'max_task_payload_size',
        'maxTaskSharedMemorySize': 'max_task_shared_memory_size',
        'maxTaskPayloadAndSharedMemorySize': 'max_task_payload_and_shared_memory_size',
        'maxMeshWorkGroupTotalCount': 'max_mesh_work_group_total_count',
        'maxMeshWorkGroupCount': 'max_mesh_work_group_count',
        'maxMeshWorkGroupInvocations': 'max_mesh_work_group_invocations',
        'maxMeshWorkGroupSize': 'max_mesh_work_group_size',
        'maxMeshSharedMemorySize': 'max_mesh_shared_memory_size',
        'maxMeshPayloadAndSharedMemorySize': 'max_mesh_payload_and_shared_memory_size',
        'maxMeshOutputMemorySize': 'max_mesh_output_memory_size',
        'maxMeshPayloadAndOutputMemorySize': 'max_mesh_payload_and_output_memory_size',
        'maxMeshOutputComponents': 'max_mesh_output_components',
        'maxMeshOutputVertices': 'max_mesh_output_vertices',
        'maxMeshOutputPrimitives': 'max_mesh_output_primitives',
        'maxMeshOutputLayers': 'max_mesh_output_layers',
        'maxMeshMultiviewViewCount': 'max_mesh_multiview_view_count',
        'meshOutputPerVertexGranularity': 'mesh_output_per_vertex_granularity',
        'meshOutputPerPrimitiveGranularity': 'mesh_output_per_primitive_granularity',
        'maxPreferredTaskWorkGroupInvocations': 'max_preferred_task_work_group_invocations',
        'maxPreferredMeshWorkGroupInvocations': 'max_preferred_mesh_work_group_invocations',
        'prefersLocalInvocationVertexOutput': 'prefers_local_invocation_vertex_output',
        'prefersLocalInvocationPrimitiveOutput': 'prefers_local_invocation_primitive_output',
        'prefersCompactVertexOutput': 'prefers_compact_vertex_output',
        'prefersCompactPrimitiveOutput': 'prefers_compact_primitive_output',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_mesh_shader',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceMeshShaderPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxTaskWorkGroupTotalCount': ctypes.c_uint32,
    'maxTaskWorkGroupCount': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxTaskWorkGroupInvocations': ctypes.c_uint32,
    'maxTaskWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxTaskPayloadSize': ctypes.c_uint32,
    'maxTaskSharedMemorySize': ctypes.c_uint32,
    'maxTaskPayloadAndSharedMemorySize': ctypes.c_uint32,
    'maxMeshWorkGroupTotalCount': ctypes.c_uint32,
    'maxMeshWorkGroupCount': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxMeshWorkGroupInvocations': ctypes.c_uint32,
    'maxMeshWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
    'maxMeshSharedMemorySize': ctypes.c_uint32,
    'maxMeshPayloadAndSharedMemorySize': ctypes.c_uint32,
    'maxMeshOutputMemorySize': ctypes.c_uint32,
    'maxMeshPayloadAndOutputMemorySize': ctypes.c_uint32,
    'maxMeshOutputComponents': ctypes.c_uint32,
    'maxMeshOutputVertices': ctypes.c_uint32,
    'maxMeshOutputPrimitives': ctypes.c_uint32,
    'maxMeshOutputLayers': ctypes.c_uint32,
    'maxMeshMultiviewViewCount': ctypes.c_uint32,
    'meshOutputPerVertexGranularity': ctypes.c_uint32,
    'meshOutputPerPrimitiveGranularity': ctypes.c_uint32,
    'maxPreferredTaskWorkGroupInvocations': ctypes.c_uint32,
    'maxPreferredMeshWorkGroupInvocations': ctypes.c_uint32,
    'prefersLocalInvocationVertexOutput': ctypes.c_uint32,
    'prefersLocalInvocationPrimitiveOutput': ctypes.c_uint32,
    'prefersCompactVertexOutput': ctypes.c_uint32,
    'prefersCompactPrimitiveOutput': ctypes.c_uint32,
}
