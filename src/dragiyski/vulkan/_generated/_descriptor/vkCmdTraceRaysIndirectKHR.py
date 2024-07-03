from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdTraceRaysIndirectKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pRaygenShaderBindingTable', 'pMissShaderBindingTable', 'pHitShaderBindingTable', 'pCallableShaderBindingTable', 'indirectDeviceAddress']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pRaygenShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
        'output': False,
    },
    'pMissShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
        'output': False,
    },
    'pHitShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
        'output': False,
    },
    'pCallableShaderBindingTable': {
        'type': CPointerType(CComplexType('VkStridedDeviceAddressRegionKHR')),
        'is_string': False,
        'output': False,
    },
    'indirectDeviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
