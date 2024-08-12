from cx_Freeze import setup, Executable
setup(
    name = "app",
    version = "0.1",
    description = "My Tkinter app",
    executables = [Executable("main.py", base="Win32GUI")]
)