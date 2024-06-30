from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVulkan13Features'
_member_list_ = ['sType', 'pNext', 'robustImageAccess', 'inlineUniformBlock', 'descriptorBindingInlineUniformBlockUpdateAfterBind', 'pipelineCreationCacheControl', 'privateData', 'shaderDemoteToHelperInvocation', 'shaderTerminateInvocation', 'subgroupSizeControl', 'computeFullSubgroups', 'synchronization2', 'textureCompressionASTC_HDR', 'shaderZeroInitializeWorkgroupMemory', 'dynamicRendering', 'shaderIntegerDotProduct', 'maintenance4']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_FEATURES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'robustImageAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'inlineUniformBlock': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingInlineUniformBlockUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pipelineCreationCacheControl': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'privateData': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDemoteToHelperInvocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderTerminateInvocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subgroupSizeControl': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'computeFullSubgroups': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'synchronization2': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'textureCompressionASTC_HDR': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderZeroInitializeWorkgroupMemory': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dynamicRendering': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderIntegerDotProduct': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maintenance4': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
