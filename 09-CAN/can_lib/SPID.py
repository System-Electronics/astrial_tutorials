import spidev

class SPID:
    def __init__(self):
        self.baudrate = 500000
        self.bits = 8
        self.mode = 0
        self.spi_port = 1

    def write(self, buf, start=0, end=None):
        if not buf:
            return
        if end is None:
            end = len(buf)

        
        self._spi = spidev.SpiDev()
        self._spi.open(self.spi_port, 0)

        
        self._spi.max_speed_hz = self.baudrate
        self._spi.mode = self.mode
        self._spi.bits_per_word = self.bits

        self._spi.writebytes2(buf[start:end])
        
        self._spi.close()
        
        return 0
    
    def readinto(self, buf, start=0, end=None, write_value=0):
        if not buf:
            return
        if end is None:
            end = len(buf)


        self._spi = spidev.SpiDev()
        self._spi.open(self.spi_port, 0)

        self._spi.max_speed_hz = self.baudrate
        self._spi.mode = self.mode
        self._spi.bits_per_word = self.bits

        data = self._spi.xfer([write_value]*(end-start))
        for i in range(end-start):  # 'readinto' the given buffer
            buf[start+i] = data[i]
    
        self._spi.close()
    
        return 0
    
    def write_readinto(self, buffer_out, buffer_in, out_start=0,
                       out_end=None, in_start=0, in_end=None):
        
        if not buffer_out or not buffer_in:
            return
        if out_end is None:
            out_end = len(buffer_out)
        if in_end is None:
            in_end = len(buffer_in)
        if out_end - out_start != in_end - in_start:
            raise RuntimeError('Buffer slices must be of equal length.')
        


        self._spi = spidev.SpiDev()
        self._spi.open(self.spi_port, 0)

        self._spi.max_speed_hz = self.baudrate
        self._spi.mode = self.mode
        self._spi.bits_per_word = self.bits


        data = self._spi.xfer(list(buffer_out[out_start:out_end+1]))
        for i in range((in_end - in_start)):
            buffer_in[i+in_start] = data[i]

        self._spi.close()

        return 0