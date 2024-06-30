from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceGroupSubmitInfo'
_member_list_ = ['sType', 'pNext', 'waitSemaphoreCount', 'pWaitSemaphoreDeviceIndices', 'commandBufferCount', 'pCommandBufferDeviceMasks', 'signalSemaphoreCount', 'pSignalSemaphoreDeviceIndices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'waitSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphoreDeviceIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['waitSemaphoreCount']],
        'is_string': False,
    },
    'commandBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCommandBufferDeviceMasks': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['commandBufferCount']],
        'is_string': False,
    },
    'signalSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSignalSemaphoreDeviceIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['signalSemaphoreCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkSubmitInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
