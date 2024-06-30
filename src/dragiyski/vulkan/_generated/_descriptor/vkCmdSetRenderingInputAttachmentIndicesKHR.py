from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetRenderingInputAttachmentIndicesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInputAttachmentIndexInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInputAttachmentIndexInfo': {
        'type': CPointerType(CComplexType('VkRenderingInputAttachmentIndexInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
