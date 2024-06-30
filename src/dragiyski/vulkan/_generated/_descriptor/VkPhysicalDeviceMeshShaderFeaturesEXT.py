from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMeshShaderFeaturesEXT'
_member_list_ = ['sType', 'pNext', 'taskShader', 'meshShader', 'multiviewMeshShader', 'primitiveFragmentShadingRateMeshShader', 'meshShaderQueries']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'taskShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'meshShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'multiviewMeshShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'primitiveFragmentShadingRateMeshShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'meshShaderQueries': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
