class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
    def power(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
        return self.__status
    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            elif self.__muted == True:
                self.__muted = False
            return self.__muted
        elif self.__status == False:
            pass
    def channel_up(self):
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            elif self.__channel == self.MIN_CHANNEL:
                self.__channel += 1
            else:
                self.__channel += 1
        elif self.__status == False:
            pass
    def channel_down(self):
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel -= 1
            elif self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        elif self.__status == False:
            pass
    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                pass
            elif self.__volume == self.MIN_VOLUME:
                self.__volume += 1
            else:
                self.__volume += 1
        elif self.__status == False:
            pass
    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                self.__volume -= 1
            elif self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        elif self.__status == False:
            pass
    def get_volume(self):
        if self.__muted == False:
            return self.__volume
        elif self.__muted == True:
            return 0
    def get_channel(self):
        return self.__channel
    def get_status(self):
        return self.__status
    def __str__(self):
        return f"Power = {self.get_status()}, Channel = {self.get_channel()}, Volume = {self.get_volume()}"



