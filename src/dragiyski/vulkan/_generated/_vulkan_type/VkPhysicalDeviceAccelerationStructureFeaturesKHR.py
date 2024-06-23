import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_uint32),
        ('accelerationStructureCaptureReplay', ctypes.c_uint32),
        ('accelerationStructureIndirectBuild', ctypes.c_uint32),
        ('accelerationStructureHostCommands', ctypes.c_uint32),
        ('descriptorBindingAccelerationStructureUpdateAfterBind', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'accelerationStructure': {'python_name': ['acceleration', 'structure']},
        'accelerationStructureCaptureReplay': {'python_name': ['acceleration', 'structure', 'capture', 'replay']},
        'accelerationStructureIndirectBuild': {'python_name': ['acceleration', 'structure', 'indirect', 'build']},
        'accelerationStructureHostCommands': {'python_name': ['acceleration', 'structure', 'host', 'commands']},
        'descriptorBindingAccelerationStructureUpdateAfterBind': {'python_name': ['descriptor', 'binding', 'acceleration', 'structure', 'update', 'after', 'bind']},
    }
}
