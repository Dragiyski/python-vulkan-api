import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perStageDescriptorSet', ctypes.c_uint32),
        ('dynamicPipelineLayout', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PER_STAGE_DESCRIPTOR_SET_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'perStageDescriptorSet': {'python_name': ['per', 'stage', 'descriptor', 'set']},
        'dynamicPipelineLayout': {'python_name': ['dynamic', 'pipeline', 'layout']},
    }
}
