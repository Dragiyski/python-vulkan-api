from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkLatencyTimingsFrameReportNV'
_member_list_ = ['sType', 'pNext', 'presentID', 'inputSampleTimeUs', 'simStartTimeUs', 'simEndTimeUs', 'renderSubmitStartTimeUs', 'renderSubmitEndTimeUs', 'presentStartTimeUs', 'presentEndTimeUs', 'driverStartTimeUs', 'driverEndTimeUs', 'osRenderQueueStartTimeUs', 'osRenderQueueEndTimeUs', 'gpuRenderStartTimeUs', 'gpuRenderEndTimeUs']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_LATENCY_TIMINGS_FRAME_REPORT_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'presentID': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'inputSampleTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'simStartTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'simEndTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'renderSubmitStartTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'renderSubmitEndTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'presentStartTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'presentEndTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'driverStartTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'driverEndTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'osRenderQueueStartTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'osRenderQueueEndTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'gpuRenderStartTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'gpuRenderEndTimeUs': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkGetLatencyMarkerInfoNV',
}
_input_of_ = set()
_output_of_ = set()
