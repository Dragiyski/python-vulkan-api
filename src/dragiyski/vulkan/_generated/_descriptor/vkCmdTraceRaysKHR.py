from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdTraceRaysKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pRaygenShaderBindingTable', 'pMissShaderBindingTable', 'pHitShaderBindingTable', 'pCallableShaderBindingTable', 'width', 'height', 'depth']
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
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
