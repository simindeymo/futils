from k import Keyboard


class Volume:
    __current_volume = None

    @staticmethod
    def current_volume():
        if Volume.__current_volume is None:
            return 0
        else:
            return Volume.__current_volume

    @staticmethod
    def __set_current_volume(volume):
        if volume > 100:
            Volume.__current_volume = 100
        elif volume < 0:
            Volume.__current_volume = 0
        else:
            Volume.__current_volume = volume

    __is_muted = False

    @staticmethod
    def is_muted():
        return Volume.__is_muted

    @staticmethod
    def __track():
        if Volume.__current_volume == None:
            Volume.__current_volume = 0
            for i in range(0, 50):
                Volume.volume_up()

    @staticmethod
    def mute():
        Volume.__track()
        Volume.__is_muted = (not Volume.__is_muted)
        Keyboard.key(Keyboard.VK_VOLUME_MUTE)

    @staticmethod
    def volume_up():
        Volume.__track()
        Volume.__set_current_volume(Volume.current_volume() + 2)
        Keyboard.key(Keyboard.VK_VOLUME_UP)

    @staticmethod
    def volume_down():
        Volume.__track()
        Volume.__set_current_volume(Volume.current_volume() - 2)
        Keyboard.key(Keyboard.VK_VOLUME_DOWN)

    @staticmethod
    def volume_set(amount):
        Volume.__track()
        if Volume.current_volume() > amount:
            for i in range(0, int((Volume.current_volume() - amount) / 2)):
                Volume.volume_down()
        else:
            for i in range(0, int((amount - Volume.current_volume()) / 2)):
                Volume.volume_up()

    @staticmethod
    def volume_min():
        Volume.volume_set(0)

    @staticmethod
    def volume_max():
        Volume.volume_set(100)
