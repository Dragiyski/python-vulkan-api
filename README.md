# dragiyski.vulkan

A ctypes binding for Vulkan API binding generated directly from the official [Vulkan-Headers](https://github.com/KhronosGroup/Vulkan-Headers) XML registry.

The project does not require any C-extensions. By default search and integrate the binding to `vulkan` library found by `ctypes.util`. This method can be overridden,
by  providing alternative `vkGetInstanceProcAddr` function, which can be any `Callable` or `int` pointer. This integrates well with vulkan loaded by external library
like `SDL_Vulkan_GetVkGetInstanceProcAddr`.

This is a low-level implementation also intended for extension. Each `ctype` is extended by a metadata. This can be used to build more "pythonic" API layer.

## Features

- **Auto-generated bindings** — structs, unions, handles, enums, commands and callbacks are all produced from the Khronos `vk.xml` / `video.xml` registry at build time.
- **Zero native dependencies at runtime** — only the Vulkan loader (e.g. `libvulkan.so`, `vulkan-1.dll`) present on the target system is required.
- **Cross-platform** — the wheel is tagged `py3-none-any`; the same file installs on Linux, Windows and macOS.
- **Layered command adapters** — `GlobalCommandAdapter`, `InstanceCommandAdapter` and `DeviceCommandAdapter` wrap `vkGetInstanceProcAddr` / `vkGetDeviceProcAddr` and lazily resolve function pointers on first access.
- **Callback helpers** — `CallbackAdapter` bridges C-style callbacks (identified by a `pUserData` pointer) to plain Python callables.

## Requirements

- Python ≥ 3.12

## Installation

TBD

## Usage

```python
from dragiyski.vulkan.binding.adapter import GlobalCommandAdapter, InstanceCommandAdapter

# Load global commands from the system Vulkan loader
vk = GlobalCommandAdapter()

# Alternative from SDL2
vk = GlobalCommandAdapter(sdl2.SDL_Vulkan_GetVkGetInstanceProcAddr().value)

# Enumerate instance extensions
count = ctypes.c_uint32(0)
vk.vkEnumerateInstanceExtensionProperties(None, count, None)

# Create a VkInstance and obtain instance-level commands
# ...
instance_vk = InstanceCommandAdapter(vk, instance_handle)
instance_vk.vkDestroyInstance(instance_handle, None)
```

All Vulkan types are available as `ctypes` subclasses and can be constructed, passed by reference, and composed into arrays exactly as in C.

## Project layout

```
src/                 # Hand-written sources (adapters, base types, helpers)
registry/            # Code generator: reads vk.xml → emits Python source files
var/registry/        # Cached copies of vk.xml and video.xml
package/             # Generated output (populated by build.py before packaging)
dist/                # Wheel / sdist output
```

## Building from source

```bash
# Install PDM (once)
pip install pdm

# Install project + dev dependencies
pdm install --dev

# Regenerate package/ from the registry XML files
pdm run build

# Produce wheel and sdist
python -m build --sdist --wheel
```

To update the local registry XML files from upstream Khronos before building:

```bash
python download.py
```

## Release

TBD

## License

LGPL — see `pyproject.toml` for details.
