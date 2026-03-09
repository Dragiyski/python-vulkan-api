import pathlib
import sys


def pdm_build_initialize(context):
    project_dir = pathlib.Path(context.root)
    project_vulkan_dir = project_dir / 'dragiyski' / 'vulkan'
    if project_vulkan_dir.exists():
        context.config.build_config['package-dir'] = ''
        return
    package_dir = project_dir / 'package'
    registry_dir = project_dir / 'registry'
    src_dir = project_dir / 'src'
    if not registry_dir.exists():
        raise FileNotFoundError(f'Registry directory not found: {registry_dir}')
    if not src_dir.exists():
        raise FileNotFoundError(f'Source directory not found: {src_dir}')
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))
    from registry import GenerateVulkanSourceFiles
    var_dir = project_dir / 'var'
    generator = GenerateVulkanSourceFiles(src_dir, package_dir, var_dir)
    generator.run()


def pdm_build_update_files(context, files):
    project_dir = pathlib.Path(context.root)
    package_dir = project_dir / 'package'
    if not package_dir.exists():
        if (project_dir / 'dragiyski' / 'vulkan').exists():
            package_dir = project_dir
        else:
            return
    files.clear()
    for src_path in package_dir.rglob('*'):
        if src_path.is_file():
            rel_path = src_path.relative_to(package_dir)
            files[str(rel_path)] = src_path
