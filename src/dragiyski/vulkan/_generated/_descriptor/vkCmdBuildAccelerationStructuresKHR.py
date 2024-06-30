from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBuildAccelerationStructuresKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'infoCount', 'pInfos', 'ppBuildRangeInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'infoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pInfos': {
        'type': CPointerType(CComplexType('VkAccelerationStructureBuildGeometryInfoKHR')),
        'is_string': False,
        'length': [['infoCount']],
    },
    'ppBuildRangeInfos': {
        'type': CPointerType(CPointerType(CComplexType('VkAccelerationStructureBuildRangeInfoKHR'))),
        'is_string': False,
        'length': [['infoCount']],
    },
}
_return_type_ = CVoidType()
