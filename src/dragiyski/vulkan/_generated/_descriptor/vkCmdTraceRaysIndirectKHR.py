from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdTraceRaysIndirectKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pRaygenShaderBindingTable', 'pMissShaderBindingTable', 'pHitShaderBindingTable', 'pCallableShaderBindingTable', 'indirectDeviceAddress']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRaygenShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
    },
    'pMissShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
    },
    'pHitShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
    },
    'pCallableShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
    },
    'indirectDeviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
