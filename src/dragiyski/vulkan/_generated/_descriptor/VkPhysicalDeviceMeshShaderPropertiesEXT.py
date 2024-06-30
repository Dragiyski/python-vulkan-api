from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMeshShaderPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'maxTaskWorkGroupTotalCount', 'maxTaskWorkGroupCount', 'maxTaskWorkGroupInvocations', 'maxTaskWorkGroupSize', 'maxTaskPayloadSize', 'maxTaskSharedMemorySize', 'maxTaskPayloadAndSharedMemorySize', 'maxMeshWorkGroupTotalCount', 'maxMeshWorkGroupCount', 'maxMeshWorkGroupInvocations', 'maxMeshWorkGroupSize', 'maxMeshSharedMemorySize', 'maxMeshPayloadAndSharedMemorySize', 'maxMeshOutputMemorySize', 'maxMeshPayloadAndOutputMemorySize', 'maxMeshOutputComponents', 'maxMeshOutputVertices', 'maxMeshOutputPrimitives', 'maxMeshOutputLayers', 'maxMeshMultiviewViewCount', 'meshOutputPerVertexGranularity', 'meshOutputPerPrimitiveGranularity', 'maxPreferredTaskWorkGroupInvocations', 'maxPreferredMeshWorkGroupInvocations', 'prefersLocalInvocationVertexOutput', 'prefersLocalInvocationPrimitiveOutput', 'prefersCompactVertexOutput', 'prefersCompactPrimitiveOutput']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxTaskWorkGroupTotalCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTaskWorkGroupCount': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxTaskWorkGroupInvocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTaskWorkGroupSize': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxTaskPayloadSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTaskSharedMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTaskPayloadAndSharedMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshWorkGroupTotalCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshWorkGroupCount': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxMeshWorkGroupInvocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshWorkGroupSize': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxMeshSharedMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshPayloadAndSharedMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshOutputMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshPayloadAndOutputMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshOutputVertices': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshOutputPrimitives': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshOutputLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMeshMultiviewViewCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'meshOutputPerVertexGranularity': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'meshOutputPerPrimitiveGranularity': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPreferredTaskWorkGroupInvocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPreferredMeshWorkGroupInvocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'prefersLocalInvocationVertexOutput': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'prefersLocalInvocationPrimitiveOutput': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'prefersCompactVertexOutput': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'prefersCompactPrimitiveOutput': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
