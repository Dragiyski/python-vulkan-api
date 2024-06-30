from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageMemoryRequirements'
_member_list_ = ['formatProperties', 'imageMipTailFirstLod', 'imageMipTailSize', 'imageMipTailOffset', 'imageMipTailStride']
_member_info_ = {
    'formatProperties': {
        'type': CComplexType('VkSparseImageFormatProperties'),
        'type_name': 'VkSparseImageFormatProperties',
        'structure': 'VkSparseImageFormatProperties',
        'is_string': False,
    },
    'imageMipTailFirstLod': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageMipTailSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'imageMipTailOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'imageMipTailStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSparseImageFormatProperties',
}
_included_in_ = {
    'VkSparseImageMemoryRequirements2',
}
_input_of_ = set()
_output_of_ = {
    'vkGetImageSparseMemoryRequirements',
}
