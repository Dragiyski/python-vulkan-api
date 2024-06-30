from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkClearValue'
_member_list_ = ['color', 'depthStencil']
_member_info_ = {
    'color': {
        'type': CComplexType('VkClearColorValue'),
        'type_name': 'VkClearColorValue',
        'union': 'VkClearColorValue',
        'is_string': False,
    },
    'depthStencil': {
        'type': CComplexType('VkClearDepthStencilValue'),
        'type_name': 'VkClearDepthStencilValue',
        'structure': 'VkClearDepthStencilValue',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkClearColorValue',
    'VkClearDepthStencilValue',
}
_included_in_ = {
    'VkClearAttachment',
    'VkRenderPassBeginInfo',
    'VkRenderingAttachmentInfo',
}
_input_of_ = set()
_output_of_ = set()
