import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('imageFormat', ctypes.c_int),
        ('flowVectorFormat', ctypes.c_int),
        ('costFormat', ctypes.c_int),
        ('outputGridSize', ctypes.c_uint32),
        ('hintGridSize', ctypes.c_uint32),
        ('performanceLevel', ctypes.c_int),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkOpticalFlowSessionCreatePrivateDataInfoNV',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateOpticalFlowSessionNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
        'imageFormat': {'python_name': ['image', 'format'], 'type': 'VkFormat'},
        'flowVectorFormat': {'python_name': ['flow', 'vector', 'format'], 'type': 'VkFormat'},
        'costFormat': {'python_name': ['cost', 'format'], 'type': 'VkFormat'},
        'outputGridSize': {'python_name': ['output', 'grid', 'size'], 'type': 'VkOpticalFlowGridSizeFlagsNV'},
        'hintGridSize': {'python_name': ['hint', 'grid', 'size'], 'type': 'VkOpticalFlowGridSizeFlagsNV'},
        'performanceLevel': {'python_name': ['performance', 'level'], 'type': 'VkOpticalFlowPerformanceLevelNV'},
        'flags': {'python_name': ['flags'], 'type': 'VkOpticalFlowSessionCreateFlagsNV'},
    }
}
