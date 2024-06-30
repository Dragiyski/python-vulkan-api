from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMeshShaderPropertiesNV'
_member_list_ = ['sType', 'pNext', 'maxDrawMeshTasksCount', 'maxTaskWorkGroupInvocations', 'maxTaskWorkGroupSize', 'maxTaskTotalMemorySize', 'maxTaskOutputCount', 'maxMeshWorkGroupInvocations', 'maxMeshWorkGroupSize', 'maxMeshTotalMemorySize', 'maxMeshOutputVertices', 'maxMeshOutputPrimitives', 'maxMeshMultiviewViewCount', 'meshOutputPerVertexGranularity', 'meshOutputPerPrimitiveGranularity']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxDrawMeshTasksCount': {
        'type': CIntType('c_uint32'),
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
    'maxTaskTotalMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTaskOutputCount': {
        'type': CIntType('c_uint32'),
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
    'maxMeshTotalMemorySize': {
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
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
