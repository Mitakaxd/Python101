from interface.start_menu import StartMenu
import ipdb

class Application:

    @classmethod
    def start(cls):
        

        StartMenu.run()
        ipdb.set_trace()

if __name__ == '__main__':
    Application.start()