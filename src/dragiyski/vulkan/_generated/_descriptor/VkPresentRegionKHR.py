from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPresentRegionKHR'
_member_list_ = ['rectangleCount', 'pRectangles']
_member_info_ = {
    'rectangleCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRectangles': {
        'type': CPointerType(CComplexType('VkRectLayerKHR')),
        'type_name': 'VkRectLayerKHR',
        'structure': 'VkRectLayerKHR',
        'length': [['rectangleCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkRectLayerKHR',
}
_included_in_ = {
    'VkPresentRegionsKHR',
}
_input_of_ = set()
_output_of_ = set()
