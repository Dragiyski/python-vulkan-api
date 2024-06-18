class VkException(Exception):
    from_code = {}

class VkError(VkException):
    pass

class VkStatus(VkException):
    pass

class VkCompressionExhaustedError(VkError):
    code = -1000338000

class VkDeviceLostError(VkError):
    code = -4

class VkExtensionNotPresentError(VkError):
    code = -7

class VkFeatureNotPresentError(VkError):
    code = -8

class VkFormatNotSupportedError(VkError):
    code = -11

class VkFragmentationError(VkError):
    code = -1000161000

class VkFragmentedPoolError(VkError):
    code = -12

class VkFullScreenExclusiveModeLostError(VkError):
    code = -1000255000

class VkImageUsageNotSupportedError(VkError):
    code = -1000023000

class VkIncompatibleDisplayError(VkError):
    code = -1000003001

class VkIncompatibleDriverError(VkError):
    code = -9

class VkInitializationFailedError(VkError):
    code = -3

class VkInvalidDrmFormatModifierPlaneLayoutError(VkError):
    code = -1000158000

class VkInvalidExternalHandleError(VkError):
    code = -1000072003

class VkInvalidOpaqueCaptureAddressError(VkError):
    code = -1000257000

class VkInvalidShaderError(VkError):
    code = -1000012000

class VkInvalidVideoStdParametersError(VkError):
    code = -1000299000

class VkLayerNotPresentError(VkError):
    code = -6

class VkMemoryMapFailedError(VkError):
    code = -5

class VkNativeWindowInUseError(VkError):
    code = -1000000001

class VkNotPermittedError(VkError):
    code = -1000174001

class VkOutOfDateError(VkError):
    code = -1000001004

class VkOutOfDeviceMemoryError(VkError):
    code = -2

class VkOutOfHostMemoryError(VkError):
    code = -1

class VkOutOfPoolMemoryError(VkError):
    code = -1000069000

class VkSurfaceLostError(VkError):
    code = -1000000000

class VkTooManyObjectsError(VkError):
    code = -10

class VkUnknownError(VkError):
    code = -13

class VkValidationFailedError(VkError):
    code = -1000011001

class VkVideoPictureLayoutNotSupportedError(VkError):
    code = -1000023001

class VkVideoProfileCodecNotSupportedError(VkError):
    code = -1000023004

class VkVideoProfileFormatNotSupportedError(VkError):
    code = -1000023003

class VkVideoProfileOperationNotSupportedError(VkError):
    code = -1000023002

class VkVideoStdVersionNotSupportedError(VkError):
    code = -1000023005

class VkEventReset(VkStatus):
    code = 4

class VkEventSet(VkStatus):
    code = 3

class VkIncompatibleShaderBinary(VkStatus):
    code = 1000482000

class VkIncomplete(VkStatus):
    code = 5

class VkNotReady(VkStatus):
    code = 1

class VkOperationDeferred(VkStatus):
    code = 1000268002

class VkOperationNotDeferred(VkStatus):
    code = 1000268003

class VkPipelineCompileRequired(VkStatus):
    code = 1000297000

class VkSuboptimal(VkStatus):
    code = 1000001003

class VkThreadDone(VkStatus):
    code = 1000268001

class VkThreadIdle(VkStatus):
    code = 1000268000

class VkTimeout(VkStatus):
    code = 2

VkException.from_code[-1000338000] = VkCompressionExhaustedError
VkException.from_code[-4] = VkDeviceLostError
VkException.from_code[-7] = VkExtensionNotPresentError
VkException.from_code[-8] = VkFeatureNotPresentError
VkException.from_code[-11] = VkFormatNotSupportedError
VkException.from_code[-1000161000] = VkFragmentationError
VkException.from_code[-12] = VkFragmentedPoolError
VkException.from_code[-1000255000] = VkFullScreenExclusiveModeLostError
VkException.from_code[-1000023000] = VkImageUsageNotSupportedError
VkException.from_code[-1000003001] = VkIncompatibleDisplayError
VkException.from_code[-9] = VkIncompatibleDriverError
VkException.from_code[-3] = VkInitializationFailedError
VkException.from_code[-1000158000] = VkInvalidDrmFormatModifierPlaneLayoutError
VkException.from_code[-1000072003] = VkInvalidExternalHandleError
VkException.from_code[-1000257000] = VkInvalidOpaqueCaptureAddressError
VkException.from_code[-1000012000] = VkInvalidShaderError
VkException.from_code[-1000299000] = VkInvalidVideoStdParametersError
VkException.from_code[-6] = VkLayerNotPresentError
VkException.from_code[-5] = VkMemoryMapFailedError
VkException.from_code[-1000000001] = VkNativeWindowInUseError
VkException.from_code[-1000174001] = VkNotPermittedError
VkException.from_code[-1000001004] = VkOutOfDateError
VkException.from_code[-2] = VkOutOfDeviceMemoryError
VkException.from_code[-1] = VkOutOfHostMemoryError
VkException.from_code[-1000069000] = VkOutOfPoolMemoryError
VkException.from_code[-1000000000] = VkSurfaceLostError
VkException.from_code[-10] = VkTooManyObjectsError
VkException.from_code[-13] = VkUnknownError
VkException.from_code[-1000011001] = VkValidationFailedError
VkException.from_code[-1000023001] = VkVideoPictureLayoutNotSupportedError
VkException.from_code[-1000023004] = VkVideoProfileCodecNotSupportedError
VkException.from_code[-1000023003] = VkVideoProfileFormatNotSupportedError
VkException.from_code[-1000023002] = VkVideoProfileOperationNotSupportedError
VkException.from_code[-1000023005] = VkVideoStdVersionNotSupportedError
VkException.from_code[4] = VkEventReset
VkException.from_code[3] = VkEventSet
VkException.from_code[1000482000] = VkIncompatibleShaderBinary
VkException.from_code[5] = VkIncomplete
VkException.from_code[1] = VkNotReady
VkException.from_code[1000268002] = VkOperationDeferred
VkException.from_code[1000268003] = VkOperationNotDeferred
VkException.from_code[1000297000] = VkPipelineCompileRequired
VkException.from_code[1000001003] = VkSuboptimal
VkException.from_code[1000268001] = VkThreadDone
VkException.from_code[1000268000] = VkThreadIdle
VkException.from_code[2] = VkTimeout
