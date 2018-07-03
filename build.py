from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="kazuki", channel="development", args="--build=missing")
    builder.add_common_builds(shared_option_name="OpenVDB:shared")

    # exclude packages that is static library for Windows
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if platform.system() != "Windows" or options["OpenVDB:shared"]:
            filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds    
    builder.run()
