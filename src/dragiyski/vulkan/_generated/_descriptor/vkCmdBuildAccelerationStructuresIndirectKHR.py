from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBuildAccelerationStructuresIndirectKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'infoCount', 'pInfos', 'pIndirectDeviceAddresses', 'pIndirectStrides', 'ppMaxPrimitiveCounts']
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
    'pIndirectDeviceAddresses': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['infoCount']],
    },
    'pIndirectStrides': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['infoCount']],
    },
    'ppMaxPrimitiveCounts': {
        'type': CPointerType(CPointerType(CIntType('c_uint32'))),
        'is_string': False,
        'length': [['infoCount']],
    },
}
_return_type_ = CVoidType()
