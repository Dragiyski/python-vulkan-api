from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetAccelerationStructureBuildSizesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'buildType', 'pBuildInfo', 'pMaxPrimitiveCounts', 'pSizeInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'buildType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pBuildInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureBuildGeometryInfoKHR')),
        'is_string': False,
    },
    'pMaxPrimitiveCounts': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['pBuildInfo', 'geometryCount']],
    },
    'pSizeInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureBuildSizesInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
