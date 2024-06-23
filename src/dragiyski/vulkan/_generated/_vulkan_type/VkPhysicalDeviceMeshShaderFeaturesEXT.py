import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('taskShader', ctypes.c_uint32),
        ('meshShader', ctypes.c_uint32),
        ('multiviewMeshShader', ctypes.c_uint32),
        ('primitiveFragmentShadingRateMeshShader', ctypes.c_uint32),
        ('meshShaderQueries', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'taskShader': {'python_name': ['task', 'shader']},
        'meshShader': {'python_name': ['mesh', 'shader']},
        'multiviewMeshShader': {'python_name': ['multiview', 'mesh', 'shader']},
        'primitiveFragmentShadingRateMeshShader': {'python_name': ['primitive', 'fragment', 'shading', 'rate', 'mesh', 'shader']},
        'meshShaderQueries': {'python_name': ['mesh', 'shader', 'queries']},
    }
}
