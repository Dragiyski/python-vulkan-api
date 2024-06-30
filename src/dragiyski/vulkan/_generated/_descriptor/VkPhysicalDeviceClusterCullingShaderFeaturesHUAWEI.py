from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI'
_member_list_ = ['sType', 'pNext', 'clustercullingShader', 'multiviewClusterCullingShader']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_FEATURES_HUAWEI',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'clustercullingShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'multiviewClusterCullingShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = {
    'VkPhysicalDeviceClusterCullingShaderVrsFeaturesHUAWEI',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
