import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstAMDX import CType as VkDeviceOrHostAddressConstAMDX

CType._fields_ = [
    ('count', ctypes.c_uint32),
    ('infos', VkDeviceOrHostAddressConstAMDX),
    ('stride', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstAMDX',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdDispatchGraphAMDX',
        'vkCmdDispatchGraphIndirectAMDX',
    },
    'output_of': set(),
    'member_map': {
        'count': {'python_name': ['count']},
        'infos': {'python_name': ['infos'], 'type': 'VkDeviceOrHostAddressConstAMDX'},
        'stride': {'python_name': ['stride']},
    }
}
