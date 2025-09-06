from ui.main_window import create_main_window
from utils.logger import Logger

if __name__ == '__main__':
    app = create_main_window()
    logger = Logger()
    logger.log("Application started")
    app.mainloop()
    logger.log("Application closed")