# Description

This is  a script to automate the testing of edge-node hardware by using UART and LoRa communications.

# Warning

This is a early version, careful set up must be made in order to work properly.

# Usage

1. Clone the repository into your host computer.

2. Connect the RS-485 of your DUT (Device under test) to your converter using a USB-TTL converter,
make sure it is connected to the port referenced as  `/dev/ttyUSB1` or change to its equivalent in the source files.

3. Connect a mesh LoRa device to the port referenced as  `dev/ttyUSB2` or change to its equivalent in the source files.

4. Make sure the LoRa device is properly set up, you can set it up with `middle-node` one execution.

5. Execute `source init.sh`, this will set up a virtual environment and download the requirements.

6. Execute `python -m unittest discover -s test` to test the device connected.

7. DUT must be have the cipher functionality enabled.

# What this code test

- LoRa functionality

- Modbus funcionality
