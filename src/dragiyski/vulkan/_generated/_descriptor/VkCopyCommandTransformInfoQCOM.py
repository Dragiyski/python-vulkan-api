from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyCommandTransformInfoQCOM'
_member_list_ = ['sType', 'pNext', 'transform']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_COMMAND_TRANSFORM_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'transform': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceTransformFlagBitsKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkBufferImageCopy2',
    'VkImageBlit2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
