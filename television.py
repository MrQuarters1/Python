class Television:
    '''
    Declaring class variables
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Declaring initial values for an object
        '''
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        '''
        :param self: referenced object
        changes status bool value
        :return none:
        '''
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False

    def mute(self) -> None:
        '''
        :param self: referenced object
        changes mute bool value
        :return none:
        '''
        if self.__status is True:
            if self.__muted is False:
                self.__muted = True
            elif self.__muted is True:
                self.__muted = False
        elif self.__status is False:
            pass

    def channel_up(self) -> None:
        '''
        :param self: referenced object
        increases channel int value by 1 unless the volume
        is at the maximum then the int value is changed to minimum
        :return none:
        '''
        if self.__status is True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            elif self.__channel == self.MIN_CHANNEL:
                self.__channel += 1
            else:
                self.__channel += 1
        elif self.__status is False:
            pass

    def channel_down(self) -> None:
        '''
        :param self: referenced object
        decreases channel int value by 1 unless the channel
        is at the minimum then the int value is changed to maximum
        :return none:
        '''
        if self.__status is True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel -= 1
            elif self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        elif self.__status is False:
            pass

    def volume_up(self) -> None:
        '''
        :param self: referenced object
        increases volume int value by 1 unless the volume
        is at the maximum then it passes
        :return none:
        '''
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                pass
            elif self.__volume == self.MIN_VOLUME:
                self.__volume += 1
            else:
                self.__volume += 1
        elif self.__status is False:
            pass

    def volume_down(self) -> None:
        '''
        :param self: referenced object
        decreases volume int value by 1 unless the volume
        is at the minimum then it passes
        :return none:
        '''
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                self.__volume -= 1
            elif self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        elif self.__status is False:
            pass

    def __str__(self) -> str:
        '''
        :param self: referenced object
        :return: status, channel, and volume (if muted, returns volume as 0) values in a formatted str
        '''
        if self.__muted is True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        elif self.__muted is False:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
