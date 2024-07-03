from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetAccelerationStructureBuildSizesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'buildType', 'pBuildInfo', 'pMaxPrimitiveCounts', 'pSizeInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'buildType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'pBuildInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureBuildGeometryInfoKHR')),
        'is_string': False,
        'output': False,
    },
    'pMaxPrimitiveCounts': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['pBuildInfo', 'geometryCount']],
        'output': False,
    },
    'pSizeInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureBuildSizesInfoKHR')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
