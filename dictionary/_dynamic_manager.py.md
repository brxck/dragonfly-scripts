# _dynamic_manager.py

command | action
--- | ---
show dynamic [(mode|modes)] status | Function(show_module_status)
enable <module> and <module2> mode only | Function(enable_modules, disableOthers=True)
enable <module> mode only | Function(enable_modules, disableOthers=True)
enable <module> mode | Function(enable_modules)
disable <module> mode | Function(disable_module)
enable <module> and <module2> and <module3> mode only | Function(enable_modules, disableOthers=True)
enable <module> and <module2> and <module3> mode | Function(enable_modules)
enable <module> and <module2> mode | Function(enable_modules)
disable [all] dynamic modes | Function(disable_all_modules)
