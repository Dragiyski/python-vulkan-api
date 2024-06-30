from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetRenderingAttachmentLocationsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pLocationInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pLocationInfo': {
        'type': CPointerType(CComplexType('VkRenderingAttachmentLocationInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
