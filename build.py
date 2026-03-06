import sys
import pathlib
from registry import GenerateVulkanSourceFiles

def main():
    project_dir = pathlib.Path(__file__).resolve().parent
    dist_dir = project_dir.joinpath('dist')
    src_dir = project_dir.joinpath('src')
    var_dir = project_dir.joinpath('var')
    generator = GenerateVulkanSourceFiles(src_dir, dist_dir, var_dir)
    generator.run()
    return 0

if __name__ == '__main__':
    sys.exit(main())
