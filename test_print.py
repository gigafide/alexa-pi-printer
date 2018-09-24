#!/usr/bin/python
from escpos.printer import Usb
p = Usb(0x0416, 0x5011)
p.text("Mini Alexa Pi Printer\n")
p.close()
