from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI'
_member_list_ = ['sType', 'pNext', 'maxWorkGroupCount', 'maxWorkGroupSize', 'maxOutputClusterCount', 'indirectBufferOffsetAlignment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_PROPERTIES_HUAWEI',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxWorkGroupCount': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxWorkGroupSize': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxOutputClusterCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'indirectBufferOffsetAlignment': {
        'type': CIntType('c_uint64'),
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
