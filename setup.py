from cx_Freeze import setup, Executable

executables = [
    Executable(script = "main.py", icon = "icon.ico")
]

buildOptions = dict(includes = ["os", "shutil"], include_files = ["README.txt", "icon.ico"])

setup(
    name = "GMod Optimizer",
    version = "1.0",
    description = "A program to optimize Garry's Mod",
    author = "toadsings",
    options = dict(build_exe = buildOptions),
    executables = executables
)