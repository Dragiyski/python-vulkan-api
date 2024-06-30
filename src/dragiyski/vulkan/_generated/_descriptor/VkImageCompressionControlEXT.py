from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageCompressionControlEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'compressionControlPlaneCount', 'pFixedRateFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCompressionFlagsEXT',
        'enum': 'VkImageCompressionFlagsEXT',
        'is_string': False,
    },
    'compressionControlPlaneCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pFixedRateFlags': {
        'type': CPointerType(CIntType('c_uint32')),
        'type_name': 'VkImageCompressionFixedRateFlagsEXT',
        'enum': 'VkImageCompressionFixedRateFlagsEXT',
        'length': [['compressionControlPlaneCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkImageCreateInfo',
    'VkPhysicalDeviceImageFormatInfo2',
    'VkSwapchainCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
