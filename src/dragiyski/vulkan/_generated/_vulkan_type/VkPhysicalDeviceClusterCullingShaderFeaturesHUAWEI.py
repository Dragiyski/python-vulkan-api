import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clustercullingShader', ctypes.c_uint32),
        ('multiviewClusterCullingShader', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': {
        'VkPhysicalDeviceClusterCullingShaderVrsFeaturesHUAWEI',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_FEATURES_HUAWEI', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'clustercullingShader': {'python_name': ['clusterculling', 'shader']},
        'multiviewClusterCullingShader': {'python_name': ['multiview', 'cluster', 'culling', 'shader']},
    }
}
