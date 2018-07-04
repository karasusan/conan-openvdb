import platform
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="OpenVDB:shared")

    # exclude packages that is dynamic library for Windows
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if platform.system() != "Windows" or not options["OpenVDB:shared"]:
            filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds    
    builder.run()
