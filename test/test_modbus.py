import serial
import unittest
from _socket import timeout

class TestSerial(unittest.TestCase):
    def test_wrong_send_crc(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            modo: slave
            baurate: 9600
            parity: Even
            stops bits: 1
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        ser.write(bytearray([1,2,3]))
        expected = bytearray([255,130,8,32,150])
        actual = ser.read(size = 5)
        self.assertEqual(actual, expected,"Must be equal")
        ser.close()
        
    def test_read_register(self):
        """
        Read first input register
        Data 0x03
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        input = bytearray([255,4,0,0,0,1,36,20])
        ser.write(input)
        expected = bytearray([255,4,2,0,0,144,228])
        actual = ser.read(size = 7 )
        self.assertEqual(actual, expected,"Must be equal")
        ser.close()
    
    def test_zero_register(self):
        
        """
        Read 0 input register
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        input = bytearray([255,4,0,0,0,0,229,212])
        ser.write(input)
        expected = bytearray([255,4,0,67,48])
        actual = ser.read(size = 5 )
        self.assertEqual(actual, expected,"Must be equal")
        ser.close()
        
    def test_wrong_id(self):
        
        """
        Read wrong ID 
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout= 1)
        input = bytearray([1,4,0,0,0,4,241,201])
        ser.write(input)
        expected = 0
        response = ser.read()
        actual = len(response)
        self.assertEqual(actual, expected,"Must be equal")
        ser.close()
    
    def test_wrong_function(self):
        
        """
        Read wrong Function
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        input = bytearray([255,1,0,0,0,4,40,23])
        ser.write(input)
        expected = bytearray([255,129,1,224,96])
        actual = ser.read(size=5)
        self.assertEqual(actual, expected,"Must be equal")
        ser.close()
    
    def test_wrong_baudarate(self):
        """
        Use wrong baudarate
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=115200,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        input = bytearray([255,4,0,0,0,1,36,20])
        ser.write(input)
        expected = bytearray([255,4,2,0,0,144,228])
        actual = ser.read(size = 7 )
        self.assertNotEqual(actual, expected,"Must be different")
        ser.close()
        
    def test_wrong_bits_quantity(self):
        """
        Use wrong bit quantity
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=115200,bytesize=serial.SEVENBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        input = bytearray([255,4,0,0,0,1,36,20])
        ser.write(input)
        expected = bytearray([255,4,2,0,0,144,228])
        actual = ser.read(size = 7 )
        self.assertNotEqual(actual, expected,"Must be different")
        ser.close()
    
    def test_wrong_bits_quantity(self):
        """
        Use wrong parity
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=115200,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout = 1)
        input = bytearray([255,4,0,0,0,1,36,20])
        ser.write(input)
        expected = bytearray([255,4,2,0,0,144,228])
        actual = ser.read(size = 7 )
        self.assertNotEqual(actual, expected,"Must be different")
        ser.close()
    
    def test_response_latency(self):
        """
        Read first input register
        Data 0x03
        """
        ser = serial.Serial("/dev/ttyUSB1", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_EVEN,stopbits=serial.STOPBITS_ONE,timeout = 1)
        
        input = bytearray([255,4,0,0,0,1,36,20])
        for i in range(100):
            ser.write(input)
            expected = bytearray([255,4,2,0,0,144,228])
            actual = ser.read(size = 7 )
            self.assertEqual(actual, expected,"Must be equal")
        ser.close()
    
    
  
if __name__ == '__main__':
    unittest.main()
    