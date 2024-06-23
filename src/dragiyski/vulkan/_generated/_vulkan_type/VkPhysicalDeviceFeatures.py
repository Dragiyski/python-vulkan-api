import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('robustBufferAccess', ctypes.c_uint32),
        ('fullDrawIndexUint32', ctypes.c_uint32),
        ('imageCubeArray', ctypes.c_uint32),
        ('independentBlend', ctypes.c_uint32),
        ('geometryShader', ctypes.c_uint32),
        ('tessellationShader', ctypes.c_uint32),
        ('sampleRateShading', ctypes.c_uint32),
        ('dualSrcBlend', ctypes.c_uint32),
        ('logicOp', ctypes.c_uint32),
        ('multiDrawIndirect', ctypes.c_uint32),
        ('drawIndirectFirstInstance', ctypes.c_uint32),
        ('depthClamp', ctypes.c_uint32),
        ('depthBiasClamp', ctypes.c_uint32),
        ('fillModeNonSolid', ctypes.c_uint32),
        ('depthBounds', ctypes.c_uint32),
        ('wideLines', ctypes.c_uint32),
        ('largePoints', ctypes.c_uint32),
        ('alphaToOne', ctypes.c_uint32),
        ('multiViewport', ctypes.c_uint32),
        ('samplerAnisotropy', ctypes.c_uint32),
        ('textureCompressionETC2', ctypes.c_uint32),
        ('textureCompressionASTC_LDR', ctypes.c_uint32),
        ('textureCompressionBC', ctypes.c_uint32),
        ('occlusionQueryPrecise', ctypes.c_uint32),
        ('pipelineStatisticsQuery', ctypes.c_uint32),
        ('vertexPipelineStoresAndAtomics', ctypes.c_uint32),
        ('fragmentStoresAndAtomics', ctypes.c_uint32),
        ('shaderTessellationAndGeometryPointSize', ctypes.c_uint32),
        ('shaderImageGatherExtended', ctypes.c_uint32),
        ('shaderStorageImageExtendedFormats', ctypes.c_uint32),
        ('shaderStorageImageMultisample', ctypes.c_uint32),
        ('shaderStorageImageReadWithoutFormat', ctypes.c_uint32),
        ('shaderStorageImageWriteWithoutFormat', ctypes.c_uint32),
        ('shaderUniformBufferArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderSampledImageArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderStorageBufferArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderStorageImageArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderClipDistance', ctypes.c_uint32),
        ('shaderCullDistance', ctypes.c_uint32),
        ('shaderFloat64', ctypes.c_uint32),
        ('shaderInt64', ctypes.c_uint32),
        ('shaderInt16', ctypes.c_uint32),
        ('shaderResourceResidency', ctypes.c_uint32),
        ('shaderResourceMinLod', ctypes.c_uint32),
        ('sparseBinding', ctypes.c_uint32),
        ('sparseResidencyBuffer', ctypes.c_uint32),
        ('sparseResidencyImage2D', ctypes.c_uint32),
        ('sparseResidencyImage3D', ctypes.c_uint32),
        ('sparseResidency2Samples', ctypes.c_uint32),
        ('sparseResidency4Samples', ctypes.c_uint32),
        ('sparseResidency8Samples', ctypes.c_uint32),
        ('sparseResidency16Samples', ctypes.c_uint32),
        ('sparseResidencyAliased', ctypes.c_uint32),
        ('variableMultisampleRate', ctypes.c_uint32),
        ('inheritedQueries', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceFeatures',
    },
    'member_map': {
        'robustBufferAccess': {'python_name': ['robust', 'buffer', 'access']},
        'fullDrawIndexUint32': {'python_name': ['full', 'draw', 'index', 'uint32']},
        'imageCubeArray': {'python_name': ['image', 'cube', 'array']},
        'independentBlend': {'python_name': ['independent', 'blend']},
        'geometryShader': {'python_name': ['geometry', 'shader']},
        'tessellationShader': {'python_name': ['tessellation', 'shader']},
        'sampleRateShading': {'python_name': ['sample', 'rate', 'shading']},
        'dualSrcBlend': {'python_name': ['dual', 'src', 'blend']},
        'logicOp': {'python_name': ['logic', 'op']},
        'multiDrawIndirect': {'python_name': ['multi', 'draw', 'indirect']},
        'drawIndirectFirstInstance': {'python_name': ['draw', 'indirect', 'first', 'instance']},
        'depthClamp': {'python_name': ['depth', 'clamp']},
        'depthBiasClamp': {'python_name': ['depth', 'bias', 'clamp']},
        'fillModeNonSolid': {'python_name': ['fill', 'mode', 'non', 'solid']},
        'depthBounds': {'python_name': ['depth', 'bounds']},
        'wideLines': {'python_name': ['wide', 'lines']},
        'largePoints': {'python_name': ['large', 'points']},
        'alphaToOne': {'python_name': ['alpha', 'to', 'one']},
        'multiViewport': {'python_name': ['multi', 'viewport']},
        'samplerAnisotropy': {'python_name': ['sampler', 'anisotropy']},
        'textureCompressionETC2': {'python_name': ['texture', 'compression', 'etc2']},
        'textureCompressionASTC_LDR': {'python_name': ['texture', 'compression', 'astc', 'ldr']},
        'textureCompressionBC': {'python_name': ['texture', 'compression', 'bc']},
        'occlusionQueryPrecise': {'python_name': ['occlusion', 'query', 'precise']},
        'pipelineStatisticsQuery': {'python_name': ['pipeline', 'statistics', 'query']},
        'vertexPipelineStoresAndAtomics': {'python_name': ['vertex', 'pipeline', 'stores', 'and', 'atomics']},
        'fragmentStoresAndAtomics': {'python_name': ['fragment', 'stores', 'and', 'atomics']},
        'shaderTessellationAndGeometryPointSize': {'python_name': ['shader', 'tessellation', 'and', 'geometry', 'point', 'size']},
        'shaderImageGatherExtended': {'python_name': ['shader', 'image', 'gather', 'extended']},
        'shaderStorageImageExtendedFormats': {'python_name': ['shader', 'storage', 'image', 'extended', 'formats']},
        'shaderStorageImageMultisample': {'python_name': ['shader', 'storage', 'image', 'multisample']},
        'shaderStorageImageReadWithoutFormat': {'python_name': ['shader', 'storage', 'image', 'read', 'without', 'format']},
        'shaderStorageImageWriteWithoutFormat': {'python_name': ['shader', 'storage', 'image', 'write', 'without', 'format']},
        'shaderUniformBufferArrayDynamicIndexing': {'python_name': ['shader', 'uniform', 'buffer', 'array', 'dynamic', 'indexing']},
        'shaderSampledImageArrayDynamicIndexing': {'python_name': ['shader', 'sampled', 'image', 'array', 'dynamic', 'indexing']},
        'shaderStorageBufferArrayDynamicIndexing': {'python_name': ['shader', 'storage', 'buffer', 'array', 'dynamic', 'indexing']},
        'shaderStorageImageArrayDynamicIndexing': {'python_name': ['shader', 'storage', 'image', 'array', 'dynamic', 'indexing']},
        'shaderClipDistance': {'python_name': ['shader', 'clip', 'distance']},
        'shaderCullDistance': {'python_name': ['shader', 'cull', 'distance']},
        'shaderFloat64': {'python_name': ['shader', 'float64']},
        'shaderInt64': {'python_name': ['shader', 'int64']},
        'shaderInt16': {'python_name': ['shader', 'int16']},
        'shaderResourceResidency': {'python_name': ['shader', 'resource', 'residency']},
        'shaderResourceMinLod': {'python_name': ['shader', 'resource', 'min', 'lod']},
        'sparseBinding': {'python_name': ['sparse', 'binding']},
        'sparseResidencyBuffer': {'python_name': ['sparse', 'residency', 'buffer']},
        'sparseResidencyImage2D': {'python_name': ['sparse', 'residency', 'image2', 'd']},
        'sparseResidencyImage3D': {'python_name': ['sparse', 'residency', 'image3', 'd']},
        'sparseResidency2Samples': {'python_name': ['sparse', 'residency2', 'samples']},
        'sparseResidency4Samples': {'python_name': ['sparse', 'residency4', 'samples']},
        'sparseResidency8Samples': {'python_name': ['sparse', 'residency8', 'samples']},
        'sparseResidency16Samples': {'python_name': ['sparse', 'residency16', 'samples']},
        'sparseResidencyAliased': {'python_name': ['sparse', 'residency', 'aliased']},
        'variableMultisampleRate': {'python_name': ['variable', 'multisample', 'rate']},
        'inheritedQueries': {'python_name': ['inherited', 'queries']},
    }
}
