import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstAMDX import CType as VkDeviceOrHostAddressConstAMDX

CType._fields_ = [
    ('nodeIndex', ctypes.c_uint32),
    ('payloadCount', ctypes.c_uint32),
    ('payloads', VkDeviceOrHostAddressConstAMDX),
    ('payloadStride', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstAMDX',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'nodeIndex': {'python_name': ['node', 'index']},
        'payloadCount': {'python_name': ['payload', 'count']},
        'payloads': {'python_name': ['payloads'], 'type': 'VkDeviceOrHostAddressConstAMDX'},
        'payloadStride': {'python_name': ['payload', 'stride']},
    }
}
