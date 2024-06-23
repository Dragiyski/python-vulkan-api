import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clusterShadingRate', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_VRS_FEATURES_HUAWEI', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'clusterShadingRate': {'python_name': ['cluster', 'shading', 'rate']},
    }
}
