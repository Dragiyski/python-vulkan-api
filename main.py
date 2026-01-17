import sys
import pathlib
from registry import GenerateVulkanSourceFiles

def main():
    target_dir = pathlib.Path(__file__).resolve().parent.joinpath('dist')
    generator = GenerateVulkanSourceFiles(target_dir)
    generator.run()
    return 0

if __name__ == '__main__':
    sys.exit(main())
