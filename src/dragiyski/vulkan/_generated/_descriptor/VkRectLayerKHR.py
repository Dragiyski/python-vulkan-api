from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRectLayerKHR'
_member_list_ = ['offset', 'extent', 'layer']
_member_info_ = {
    'offset': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'extent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'layer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
    'VkOffset2D',
}
_included_in_ = {
    'VkPresentRegionKHR',
}
_input_of_ = set()
_output_of_ = set()
