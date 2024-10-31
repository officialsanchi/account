class Television:
    def __init__(self):
        self.is_on = True
        self.__channel = 99
        self.__volume = 1

    def turn_on(self):
        return self.is_on

    def turn_off(self):
        self.is_on = False

    def volume_up(self):
        return self.__volume
    def set_volume(self, volume):
        if volume < 1 & volume > 10:
            return 0
        self.__volume = volume

    def channel(self):
        return self.__channel










