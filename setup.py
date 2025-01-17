from cx_Freeze import setup, Executable
import distutils

build_exe_options = {
    "includes": ["Dependencias.importaciones"],
    "include_files": ["Dependencias"]
}
setup(
    name="POU3",
    version="1.0",
    description="pou3",
    options={"build_exe": build_exe_options},
    executables=[Executable("CopiaPou3.py", base=None)]
)