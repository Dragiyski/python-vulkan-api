import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useMaxLevelIdc', ctypes.c_uint32),
        ('maxLevelIdc', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkVideoSessionCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'useMaxLevelIdc': {'python_name': ['use', 'max', 'level', 'idc']},
        'maxLevelIdc': {'python_name': ['max', 'level', 'idc'], 'type': 'StdVideoH265LevelIdc'},
    }
}
