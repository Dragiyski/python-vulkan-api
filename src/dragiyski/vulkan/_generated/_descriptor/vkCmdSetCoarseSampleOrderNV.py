from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetCoarseSampleOrderNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'sampleOrderType', 'customSampleOrderCount', 'pCustomSampleOrders']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'sampleOrderType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'customSampleOrderCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCustomSampleOrders': {
        'type': CPointerType(CComplexType('VkCoarseSampleOrderCustomNV')),
        'is_string': False,
        'length': [['customSampleOrderCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
