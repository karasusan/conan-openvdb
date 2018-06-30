from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="kazuki", channel="development", args="--build=missing")
    builder.add_common_builds(shared_option_name="OpenVDB:shared")
    builder.run()
