## export the file .exe in python
    Step 1: Install cx_Freeze
    >> pip install cx_Freeze
    Step 2 : Create a setup script (setup.py):
    from cx_Freeze import setup, Executable
    setup(
        name = "app",
        version = "0.1",
        description = "My Tkinter app",
        executables = [Executable("app.py", base="Win32GUI")]
    )
    Step 3: Run
    >> python setup.py build




# common
