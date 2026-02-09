"""
We talk to the Newport Velocity TLB6700 using a driver (generally located at 
C:\\Program Files\\Newport\\USB Driver\\Bin\\UsbDll.dll) instead of a standard 
serial library. This driver **needs a device number in order to communicate 
with a device**. The device numbers of the connected devices can be extracted 
using this:

>>> from newport_tlb6700 import NewportUSB, TLB6700, list_devices
>>> usb = NewportUSB()
>>> usb.init_system()
>>> devices = usb.list_devices()
>>> for device_id, description in devices:
>>>     print(f'  Device {device_id}: {description}')

Then, the device can be communicated with:

>>> laser = TLB6700(<desired device id>, usb)
>>> print(laser.get_identification())

Locating the Driver
-------------------

If the code above runs and shows devices, then everything works! Windows will
check for `UsbDll.dll` in several places (current directory, PATH, etc)

If it does not find the driver automatically please:
    1. Confirm that you have downloaded the Newport Velocity `laser driver`_.
    2. Try passing the path of the driver explicitly to NewportUSB

>>> usb = NewportUSB('C:\\Program Files\\Newport\\USB Driver\\Bin\\UsbDll.dll')

.. _laser driver: https://www.newport.com/f/velocity-wide-&-fine-tunable-lasers
"""
from .tlb6700 import TLB6700, NewportUSB
