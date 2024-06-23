import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureInfoNV import CType as VkAccelerationStructureInfoNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('compactedSize', ctypes.c_uint64),
    ('info', VkAccelerationStructureInfoNV),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    },
    'includes': {
        'VkAccelerationStructureInfoNV',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateAccelerationStructureNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'compactedSize': {'python_name': ['compacted', 'size']},
        'info': {'python_name': ['info'], 'type': 'VkAccelerationStructureInfoNV'},
    }
}
