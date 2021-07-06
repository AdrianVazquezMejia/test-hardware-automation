import serial
import unittest
from _socket import timeout
from functools import reduce
from cipher import *
import time
#FF 0F 00 01 00 03 01 07 7D 9D
# FF 0F 00 01 00 03 51 D4
class TestLoRa(unittest.TestCase):
    def test_modbus_response(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB0", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
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
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB0", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 14, 0, 255, 0, 7, 1, 8]
        payload =[255,4,0,0,0,1,36,20]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        input_frame.append(check_sum)
        
        #for i in range(100):
        ser.write(bytearray(input_frame))
        result = ser.read(size =8)
        expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
        self.assertEqual(result, expected,"Must be equal")
        
        result = ser.read(size=16)
        result = result[8:15]
        actual = decrypt_md(result, "CFB")
        expected = bytearray([255,4,2,0,0,144,228])
        self.assertEqual(actual, expected,"Must be equal")

    def test_modbus_response_write_sigle_coil(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB0", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 14, 0, 255, 0, 7, 1, 8]
        payload =[255,5,0,255,255,0,169,212]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        
        input_frame.append(check_sum)
        ser.write(bytearray(input_frame))
        result = ser.read(size =8)
        
        expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
        self.assertEqual(result, expected,"Must be equal")
        
        result = ser.read(size=16)
        result = result[8:16]
        actual = decrypt_md(result, "CFB")
        expected = bytearray([255,5,0,255,255,0,169,212])
        self.assertEqual(actual, expected,"Must be equal")

    def test_modbus_response_write_multiples_coils(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB0", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 16, 0, 255, 0, 7, 1, 10]
        payload =[255, 15, 0, 1, 0, 3, 1, 7, 125, 157]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        
        input_frame.append(check_sum)
        ser.write(bytearray(input_frame))
        result = ser.read(size =8)
        
        expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
        self.assertEqual(result, expected,"Must be equal")
        
        result = ser.read(size=16)
        result = result[8:16]
        actual = decrypt_md(result, "CFB")
        expected = bytearray([255,15, 0, 1, 0, 3, 81, 212])
        self.assertEqual(actual, expected,"Must be equal")

    def test_modbus_response_write_coil_slave(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB0", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 14, 0, 255, 0, 7, 1, 8]
        payload =[1,5,0,1,255,0,221,250]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        
        input_frame.append(check_sum)
        ser.write(bytearray(input_frame))
        result = ser.read(size =8)
        
        expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
        self.assertEqual(result, expected,"Must be equal")
        
        result = ser.read(size=16)
        result = result[8:16]
        actual = decrypt_md(result, "CFB")
        expected = bytearray([1,5,0,1,255,0,221,250])
        self.assertEqual(actual, expected,"Must be equal")

    def test_modbus_response_write_sigle_reset(self):
        """
        Wrong CRC Response test
            CONDITIONS: 
            id 255
            lora: configurado
            baurate: 9600
            puerto : /dev/tty/USB0
        """
        ser = serial.Serial("/dev/ttyUSB0", baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout =2)
        pre_frame = [5, 0, 1, 16, 0, 255, 0, 7, 1, 8]
        payload =[255,5,0,0,255,0,153,228]
        payload = encrypt_md(payload, "CFB")
        input_frame = pre_frame + payload
        check_sum = reduce(lambda x, y: x ^ y, input_frame)
        
        input_frame.append(check_sum)
        ser.write(bytearray(input_frame))
        result = ser.read(size =8)
        
        expected = bytearray([5, 0, 129, 3, 0, 255, 0, 120])
        self.assertEqual(result, expected,"Must be equal")
        
        result = ser.read(size=16)
        result = result[8:16]
        actual = decrypt_md(result, "CFB")
        expected = bytearray([])
        self.assertEqual(actual, expected,"Must be equal")
  
if __name__ == '__main__':
    unittest.main()
    
