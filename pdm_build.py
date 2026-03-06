import pathlib
import sys


def pdm_build_initialize(context):
    project_dir = pathlib.Path(context.root)
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))
    from registry import GenerateVulkanSourceFiles
    src_dir = project_dir / 'src'
    package_dir = project_dir / 'package'
    var_dir = project_dir / 'var'
    generator = GenerateVulkanSourceFiles(src_dir, package_dir, var_dir)
    generator.run()


def pdm_build_update_files(context, files):
    project_dir = pathlib.Path(context.root)
    package_dir = project_dir / 'package'
    if not package_dir.exists():
        return
    for src_path in package_dir.rglob('*'):
        if src_path.is_file():
            rel_path = src_path.relative_to(package_dir)
            files[str(rel_path)] = src_path
