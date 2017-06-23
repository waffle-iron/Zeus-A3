from sys import platform as _platform
from subprocess import check_output as callcmd
import tkinter as tk
import tkinter.ttk as ttk

def installed():
    "Checks if the module is installed"
    try:
        import mysql.connector
    except ImportError:
        return false
    else:
        return true

def ensureins():
    "Ensures that the module is ready to be used"
    if not installed():
        inswin = tk.Tk()
        inswin.title("Install MySQL Connector")
        proclab = tk.Message(inswin, text="Please wait while Zeus installs the database connection library.")
        proclab.grid(row=0)
        inswin.update()

        if _platform == "linux" or _platform == "linux2":
            # linux
            try:
                callcmd("sudo dpkg -i mysql/debian.deb", shell=True)
            except:
                proclab.config(text="The package could not be installed. Please run Zeus with sudo privileges to continue.")
                inswin.update()
            else:
                inswin.destroy()
        elif _platform == "darwin":
            # MAC OS X
            proclab.config(text="""As you are using an Apple OSX computer, you will need to install the MySQL connector package manually. Please follow the instructions below to install the package, then click the continue button.

                           Go to the Zeus A3 installation directory. Then, navigate down into the setup folder - then into mysql. Open macos.dmg, then run the .pkg file by double-clicking it.""")
            def cont():
                "Destroys the window"
                inswin.destroy()
            contbutton = ttk.Button(inswin, text="Continue", command=cont, state="disabled")
            contbutton.grid(row=1, sticky=tk.E+tk.W)
            inswin.update()
        elif _platform == "win32":
            # Windows
            try:
                callcmd("msiexec /i mysql/windows32.msi", shell=True)
            except:
                proclab.config(text="Could not install the package. Please get administrator privileges to continue.")
                inswin.update()
            else:
                inswin.destroy()
        elif _platform == "win64":
            # Windows 64-bit
            try:
                callcmd("msiexec /i mysql/windows64.msi", shell=True)
            except:
                proclab.config(text="Could not install the package. Please get administrator privileges to continue.")
                inswin.update()
            else:
                inswin.destroy()
