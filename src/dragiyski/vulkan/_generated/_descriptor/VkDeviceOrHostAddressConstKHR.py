from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkDeviceOrHostAddressConstKHR'
_member_list_ = ['deviceAddress', 'hostAddress']
_member_info_ = {
    'deviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hostAddress': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkAccelerationStructureGeometryAabbsDataKHR',
    'VkAccelerationStructureGeometryInstancesDataKHR',
    'VkAccelerationStructureGeometryMotionTrianglesDataNV',
    'VkAccelerationStructureGeometryTrianglesDataKHR',
    'VkAccelerationStructureTrianglesDisplacementMicromapNV',
    'VkAccelerationStructureTrianglesOpacityMicromapEXT',
    'VkCopyMemoryToAccelerationStructureInfoKHR',
    'VkCopyMemoryToMicromapInfoEXT',
    'VkMicromapBuildInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
