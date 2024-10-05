from pca9685_driver import Device

class PWMChannel:
    """A single PCA9685 channel that matches the :py:class:`~pwmio.PWMOut` API.

    :param PCA9685 pca: The PCA9685 object
    :param int index: The index of the channel
    """

    def __init__(self, pca: "PCA9685", index: int):
        self._pca = pca
        self._index = index

    @property
    def frequency(self) -> float:
        """The overall PWM frequency in Hertz (read-only).
        A PWMChannel's frequency cannot be set individually.
        All channels share a common frequency, set by PCA9685.frequency."""
        return self._pca.frequency

    @frequency.setter
    def frequency(self, _):
        raise NotImplementedError("frequency cannot be set on individual channels")

    @property
    def duty_cycle(self) -> int:
        """16 bit value that dictates how much of one cycle is high (1) versus low (0). 0xffff will
        always be high, 0 will always be low and 0x7fff will be half high and then half low.
        """
        return self._pca.device.get_pwm(self._index)

    @duty_cycle.setter
    def duty_cycle(self, value: int) -> None:
        if not 0 <= value <= 0xFFFF:
            raise ValueError(f"Out of range: value {value} not 0 <= value <= 65,535")

        value = value >> 4
        self._pca.device.set_pwm(self._index, value)

class PCAChannels:  # pylint: disable=too-few-public-methods
    """Lazily creates and caches channel objects as needed. Treat it like a sequence.

    :param PCA9685 pca: The PCA9685 object
    """

    def __init__(self, pca: "PCA9685") -> None:
        self._pca = pca
        self._channels = [None] * len(self)

    def __len__(self) -> int:
        return 16

    def __getitem__(self, index: int) -> PWMChannel:
        if not self._channels[index]:
            self._channels[index] = PWMChannel(self._pca, index)
        return self._channels[index]

class PCA9685:
    def __init__(
        self,
        *,
        bus: int = 4,
        address: int = 0x40,
        reference_clock_speed: int = 25000000,
    ) -> None:
        self.device = Device(address, bus_number=bus)
        self.reference_clock_speed = reference_clock_speed
        """The reference clock speed in Hz."""
        self.channels = PCAChannels(self)

    @property
    def frequency(self) -> float:
        """The overall PWM frequency in Hertz."""
        prescale_result = self.prescale
        if prescale_result < 3:
            raise ValueError(
                "The device pre_scale register (0xFE) was not read or returned a value < 3"
            )
        return self.reference_clock_speed / 4096 / (prescale_result + 1)

    @frequency.setter
    def frequency(self, freq: float) -> None:
        prescale = int(self.reference_clock_speed / 4096.0 / freq + 0.5) - 1
        if prescale < 3:
            raise ValueError("PCA9685 cannot output at the given frequency")
        
        self.prescale = prescale
        self.device.set_pwm_frequency(freq)

    def __enter__(self) -> "PCA9685":
        return self
    
    def __exit__(self) -> None:
        print("Exiting")