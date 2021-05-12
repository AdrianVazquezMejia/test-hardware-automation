import serial
import unittest
from _socket import timeout
from functools import reduce
from cipher import *
import time
class TestLoRa(unittest.TestCase):
    def test_modbus_response(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB2
        """
        ser = serial.Serial("/dev/ttyUSB2", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 14, 0, 255, 0, 7, 1, 8]
        payload =[255,4,0,0,0,1,36,20]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        
        input_frame.append(check_sum)
        ser.write(bytearray(input_frame))
        result = ser.read(size =8)
        
        expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
        self.assertEqual(result, expected,"Must be equal")
        
        result = ser.read(size=16)
        result = result[8:15]
        actual = decrypt_md(result, "CFB")
        expected = bytearray([255,4,2,0,0,144,228])
        self.assertEqual(actual, expected,"Must be equal")
        
    def test_modbus_response_latency(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB2
        """
        ser = serial.Serial("/dev/ttyUSB2", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 14, 0, 255, 0, 7, 1, 8]
        payload =[255,4,0,0,0,1,36,20]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        input_frame.append(check_sum)
        
        for i in range(100):
            ser.write(bytearray(input_frame))
            result = ser.read(size =8)
            expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
            self.assertEqual(result, expected,"Must be equal")
            
            result = ser.read(size=16)
            result = result[8:15]
            actual = decrypt_md(result, "CFB")
            expected = bytearray([255,4,2,0,0,144,228])
            self.assertEqual(actual, expected,"Must be equal")

  
if __name__ == '__main__':
    unittest.main()
    