from fbs_runtime.application_context.PySide6 import ApplicationContext

import sys

from package.main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    # with a context one can get access to resources using the filename
    # e.g., in main_window.py: self.ctx.get_resource("style.css")
    window = MainWindow(ctx=appctxt)
    window.resize(550, 600)              # bigger size of the final app
    window.show()
    exit_code = appctxt.app.exec()       # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)