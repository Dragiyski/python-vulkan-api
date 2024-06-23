import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustImageAccess', ctypes.c_uint32),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
        ('pipelineCreationCacheControl', ctypes.c_uint32),
        ('privateData', ctypes.c_uint32),
        ('shaderDemoteToHelperInvocation', ctypes.c_uint32),
        ('shaderTerminateInvocation', ctypes.c_uint32),
        ('subgroupSizeControl', ctypes.c_uint32),
        ('computeFullSubgroups', ctypes.c_uint32),
        ('synchronization2', ctypes.c_uint32),
        ('textureCompressionASTC_HDR', ctypes.c_uint32),
        ('shaderZeroInitializeWorkgroupMemory', ctypes.c_uint32),
        ('dynamicRendering', ctypes.c_uint32),
        ('shaderIntegerDotProduct', ctypes.c_uint32),
        ('maintenance4', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_FEATURES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'robustImageAccess': {'python_name': ['robust', 'image', 'access']},
        'inlineUniformBlock': {'python_name': ['inline', 'uniform', 'block']},
        'descriptorBindingInlineUniformBlockUpdateAfterBind': {'python_name': ['descriptor', 'binding', 'inline', 'uniform', 'block', 'update', 'after', 'bind']},
        'pipelineCreationCacheControl': {'python_name': ['pipeline', 'creation', 'cache', 'control']},
        'privateData': {'python_name': ['private', 'data']},
        'shaderDemoteToHelperInvocation': {'python_name': ['shader', 'demote', 'to', 'helper', 'invocation']},
        'shaderTerminateInvocation': {'python_name': ['shader', 'terminate', 'invocation']},
        'subgroupSizeControl': {'python_name': ['subgroup', 'size', 'control']},
        'computeFullSubgroups': {'python_name': ['compute', 'full', 'subgroups']},
        'synchronization2': {'python_name': ['synchronization2']},
        'textureCompressionASTC_HDR': {'python_name': ['texture', 'compression', 'astc', 'hdr']},
        'shaderZeroInitializeWorkgroupMemory': {'python_name': ['shader', 'zero', 'initialize', 'workgroup', 'memory']},
        'dynamicRendering': {'python_name': ['dynamic', 'rendering']},
        'shaderIntegerDotProduct': {'python_name': ['shader', 'integer', 'dot', 'product']},
        'maintenance4': {'python_name': ['maintenance4']},
    }
}
