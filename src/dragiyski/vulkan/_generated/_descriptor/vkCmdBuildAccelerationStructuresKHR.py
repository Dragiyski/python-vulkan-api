from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBuildAccelerationStructuresKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'infoCount', 'pInfos', 'ppBuildRangeInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'infoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pInfos': {
        'type': CPointerType(CComplexType('VkAccelerationStructureBuildGeometryInfoKHR')),
        'is_string': False,
        'length': [['infoCount']],
        'output': False,
    },
    'ppBuildRangeInfos': {
        'type': CPointerType(CPointerType(CComplexType('VkAccelerationStructureBuildRangeInfoKHR'))),
        'is_string': False,
        'length': [['infoCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
