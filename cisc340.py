# import board, digitalio, busio
# import time
# import neopixel
# #import adafruit_sdcard, storage
# #import os

# #spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# # Use board.SD_CS for Feather M0 Adalogger
# #cs = digitalio.DigitalInOut(board.SD_CS)
# #sdcard = adafruit_sdcard.SDCard(spi, cs)
# #vfs = storage.VfsFat(sdcard)
# #storage.mount(vfs, "/sd")
# #with open("/sd/test.txt", "w") as f:
# #    f.write("Hello world!\r\n")


# # Use any pin that is not taken by SPI
# # SD_CS = board.A0
 
# # # Connect to the card and mount the filesystem.
# # spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# # cs = digitalio.DigitalInOut(SD_CS)
# # sdcard = adafruit_sdcard.SDCard(spi, cs)
# # vfs = storage.VfsFat(sdcard)
# # storage.mount(vfs, "/sd")

# # led = digitalio.DigitalInOut(board.D13)
# # led.direction = digitalio.Direction.OUTPUT

# led = neopixel.NeoPixel(board.NEOPIXEL, 1)

# # uart = busio.UART(board.TX, board.RX, baudrate=115200)

# # def print_directory(path, tabs=0):
# #     for file in os.listdir(path):
# #         stats = os.stat(path + "/" + file)
# #         filesize = stats[6]
# #         isdir = stats[0] & 0x4000
 
# #         if filesize < 1000:
# #             sizestr = str(filesize) + " by"
# #         elif filesize < 1000000:
# #             sizestr = "%0.1f KB" % (filesize / 1000)
# #         else:
# #             sizestr = "%0.1f MB" % (filesize / 1000000)
 
# #         prettyprintname = ""
# #         for _ in range(tabs):
# #             prettyprintname += "   "
# #         prettyprintname += file
# #         if isdir:
# #             prettyprintname += "/"
# #         print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))
 
# #         # recursively print directory contents
# #         if isdir:
# #             print_directory(path + "/" + file, tabs + 1)


# def wheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if pos < 0 or pos > 255:
#         return 0, 0, 0
#     if pos < 85:
#         return int(255 - pos * 3), int(pos * 3), 0
#     if pos < 170:
#         pos -= 85
#         return 0, int(255 - pos * 3), int(pos * 3)
#     pos -= 170
#     return int(pos * 3), 0, int(255 - (pos * 3))


# led.brightness = 0.3
 
# i = 0


# while True:
#     # led.value = True
#     # time.sleep(1)
#     # led.value = False
#     # time.sleep(1)
#     # print("hello")

#     # print("Files on filesystem:")
#     # print("====================")
#     # print_directory("/sd")

#     # rgb.brightness()
#     # rgb[0] = (255, 0, 0)
#     # time.sleep(0.5)
#     # rgb[0] = (0, 255, 0)
#     # time.sleep(0.5)
#     # rgb[0] = (0, 0, 255)
#     # time.sleep(0.5)
#     # rgb.brightness(0)

#   #   color = [(100,200,100), (255,1,20)]
#   #   for i in color:
#       # rgb[0] = i
#       # time.sleep(0.1)

#     i = (i + 1) % 256  # run from 0 to 255
#     led.fill(wheel(i))
#     time.sleep(0.1)





















# import time
 
# import board
# import neopixel
 
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
# pixels.fill((0, 0, 0))
# pixels.show()
 
# # choose which demos to play
# # 1 means play, 0 means don't!
# simpleCircleDemo = 1
# flashDemo = 1
# rainbowDemo = 1
# rainbowCycleDemo = 1
 
 
# def wheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if pos < 85:
#         return (int(pos * 3), int(255 - (pos * 3)), 0)
#     elif pos < 170:
#         pos -= 85
#         return (int(255 - (pos * 3)), 0, int(pos * 3))
#     else:
#         pos -= 170
#         return (0, int(pos * 3), int(255 - pos * 3))
 
 
# def rainbow_cycle(wait):
#     for j in range(255):
#         for i in range(len(pixels)):
#             idx = int((i * 256 / len(pixels)) + j * 10)
#             pixels[i] = wheel(idx & 255)
#         pixels.show()
#         time.sleep(wait)
 
 
# def rainbow(wait):
#     for j in range(255):
#         for i in range(len(pixels)):
#             idx = int(i + j)
#             pixels[i] = wheel(idx & 255)
#         pixels.show()
#         time.sleep(wait)
 
 
# def simpleCircle(wait):
#     RED = 0x100000  # (0x10, 0, 0) also works
#     YELLOW = (0x10, 0x10, 0)
#     GREEN = (0, 0x10, 0)
#     AQUA = (0, 0x10, 0x10)
#     BLUE = (0, 0, 0x10)
#     PURPLE = (0x10, 0, 0x10)
#     BLACK = (0, 0, 0)
 
#     for i in range(len(pixels)):
#         pixels[i] = RED
#         time.sleep(wait)
#     time.sleep(1)
 
#     for i in range(len(pixels)):
#         pixels[i] = YELLOW
#         time.sleep(wait)
#     time.sleep(1)
 
#     for i in range(len(pixels)):
#         pixels[i] = GREEN
#         time.sleep(wait)
#     time.sleep(1)
 
#     for i in range(len(pixels)):
#         pixels[i] = AQUA
#         time.sleep(wait)
#     time.sleep(1)
 
#     for i in range(len(pixels)):
#         pixels[i] = BLUE
#         time.sleep(wait)
#     time.sleep(1)
 
#     for i in range(len(pixels)):
#         pixels[i] = PURPLE
#         time.sleep(wait)
#     time.sleep(1)
 
#     for i in range(len(pixels)):
#         pixels[i] = BLACK
#         time.sleep(wait)
#     time.sleep(1)
 
 
# while True:
#     # if simpleCircleDemo:
#     #     print('Simple Circle Demo')
#     #     simpleCircle(.05)
 
#     # if flashDemo:  # this will play if flashDemo = 1 up above
#     #     print('Flash Demo')
#     #     pixels.fill((255, 0, 0))
#     #     pixels.show()
#     #     time.sleep(.25)
 
#     #     pixels.fill((0, 255, 0))
#     #     pixels.show()
#     #     time.sleep(.25)
 
#     #     pixels.fill((0, 0, 255))
#     #     pixels.show()
#     #     time.sleep(.25)
 
#     #     pixels.fill((255, 255, 255))
#     #     pixels.show()
#     #     time.sleep(.25)
 
#     # if rainbowDemo:
#     #     print('Rainbow Demo')
#     #     rainbow(.001)
 
#     if rainbowCycleDemo:
#         print('Rainbow Cycle Demo')
#         rainbow_cycle(.001)

















# import os
# import board, busio, digitalio, time, pulseio
# import adafruit_sdcard, storage, adafruit_thermistor

# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# cs = digitalio.DigitalInOut(board.SCL)
# sdcard = adafruit_sdcard.SDCard(spi, cs)
# vfs = storage.VfsFat(sdcard)
# storage.mount(vfs, "/sd")
# thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
# led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)

# def delFile(path):
#     #path is: "/sd/filenamehere"
#     os.remove(path)

# def printDirectory(path, tabs=0):
#     for file in os.listdir(path):
#         stats = os.stat(path + "/" + file)
#         filesize = stats[6]
#         isdir = stats[0] & 0x4000
 
#         if filesize < 1000:
#             sizestr = str(filesize) + " by"
#         elif filesize < 1000000:
#             sizestr = "%0.1f KB" % (filesize / 1000)
#         else:
#             sizestr = "%0.1f MB" % (filesize / 1000000)
 
#         prettyprintname = ""
#         for _ in range(tabs):
#             prettyprintname += "   "
#         prettyprintname += file
#         if isdir:
#             prettyprintname += "/"
#         print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

#         if isdir:
#             printDirectory(path + "/" + file, tabs + 1)

# def display():
#     for i in range(100):
#         # PWM LED up and down
#         if i < 50:
#             led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
#         else:
#             led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
#         time.sleep(0.01)

# print("Files on filesystem:")
# print("====================")
# printDirectory("/sd")

# while True:
#     with open("/sd/t.txt", "a") as f:
#         display()
#         temp_c = thermistor.temperature
#         temp_f = temp_c * 9 / 5 + 32
#         print("Temperature is: %f C and %f F" % (temp_c, temp_f))
#         f.write(str(temp_c)+"#"+str(temp_f)+"\n")
#     time.sleep(5)






























# import time, board, neopixel
 
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)
# # pixels.fill((0, 0, 0))
# # pixels.show()

# def wheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if pos < 85:
#         return (int(pos * 3), int(255 - (pos * 3)), 0)
#     elif pos < 170:
#         pos -= 85
#         return (int(255 - (pos * 3)), 0, int(pos * 3))
#     else:
#         pos -= 170
#         return (0, int(pos * 3), int(255 - pos * 3))

# def rainbow_cycle(wait):
#     for j in range(255):
#         for i in range(len(pixels)):
#             idx = int((i * 256 / len(pixels)) + j * 10)
#             pixels[i] = wheel(idx & 255)
#         pixels.show()
#         time.sleep(wait)

# while True: 
#     rainbow_cycle(.001)




















# import time, board, neopixel
# from analogio import AnalogIn

# # pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)
# # pixels.fill((255, 255, 255))

# heartBeat = AnalogIn(board.A5)

# # pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1)
# # light = AnalogIn(board.LIGHT)
# # pixels[1] = (0, 255, 0)
# # NUM_OVERSAMPLE = 10
# # NUM_SAMPLES = 20
# # samples = [0] * NUM_SAMPLES

# while True:
#     # pixels.show()
#     print((heartBeat.value * 3.3) / 65536)
#     time.sleep(0.1)

# # while True:
# #     for i in range(NUM_SAMPLES):
# #         oversample = 0
# #         for s in range(NUM_OVERSAMPLE):
# #             oversample += float(light.value)
# #         samples[i] = oversample / NUM_OVERSAMPLE
# #         mean = sum(samples) / float(len(samples))
# #         print(samples[i] - mean)
# #         time.sleep(0.1)



















# import time, board, digitalio, neopixel, adafruit_thermistor, busio, os, adafruit_sdcard, storage
# from analogio import AnalogIn

# #show heartbeat
# led = digitalio.DigitalInOut(board.D13)
# led.direction = digitalio.Direction.OUTPUT

# #start counting
# buttonA = digitalio.DigitalInOut(board.BUTTON_A)
# buttonA.direction = digitalio.Direction.INPUT
# buttonA.pull = digitalio.Pull.DOWN

# #start logging
# buttonB = digitalio.DigitalInOut(board.BUTTON_B)
# buttonB.direction = digitalio.Direction.INPUT
# buttonB.pull = digitalio.Pull.DOWN

# #show counting time
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01)

# # resistor = 10000
# # resistance = 10000
# # nominal_temp = 25
# # b_coefficient = 3950
# # adafruit_thermistor.Thermistor(pin, series_resistor, nominal_resistance, nominal_temperature, b_coefficient, *, high_side=True)
# thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

# # spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# # cs = digitalio.DigitalInOut(board.SCL)
# # sdcard = adafruit_sdcard.SDCard(spi, cs)
# # vfs = storage.VfsFat(sdcard)
# # storage.mount(vfs, "/sd")

# heartBeat = AnalogIn(board.A5)
# # convert from arduino to int(550/1024*65535) = 35199
# threshold = 35199

# def blink(pause=0.3, c=3):
#     # (0, 255, 0) green (0,0xBF,0x11)
#     for i in range(0, c):
#         pixels.fill((0, 255, 0))
#         pixels.show()
#         time.sleep(pause)
#         pixels.fill((0,0,0))
#         pixels.show()
#         time.sleep(pause)

# def heartbeatCount(hb, pause=0.01):
#     print("START!")
#     count, p = 0, 1
#     while count < 600:
#         if count % 60 == 0:
#             for i in range(0, p):
#                 pixels[i] = (255, 255, 255)
#             pixels.show()
#             p += 1
#         # hb = heartBeat.value
#         # print(hb)
#         if hb >= 35199:
#             led.value = True
#         else:
#             led.value = False
#         time.sleep(pause)
#         print(count)
#         count += 1
#     led.value = False
#     print("END!")
#     blink()

# # def heartbeatPulse(hb):
# #     # How many light readings per sample
# #     NUM_OVERSAMPLE = 10
# #     # How many samples we take to calculate 'average'
# #     NUM_SAMPLES = 20
# #     samples = [0] * NUM_SAMPLES
# #     for i in range(NUM_SAMPLES):
# #         # Take NUM_OVERSAMPLE number of readings really fast
# #         oversample = 0
# #         for s in range(NUM_OVERSAMPLE):
# #             oversample += float(hb)
# #         # and save the average from the oversamples
# #         samples[i] = oversample / NUM_OVERSAMPLE  # Find the average
 
# #         mean = sum(samples) / float(len(samples))  # take the average
# #         print(samples[i] - mean)  # 'center' the reading
# #         time.sleep(0.025)  # change to go faster/slower

# def temperature(pause=1):
#     c = thermistor.temperature
#     f = c * 9 / 5 + 32
#     print("Temperature is: %f C and %f F" % (c, f))
#     time.sleep(pause)

# def printDirectoryHelper(path, tabs=0):
#     for file in os.listdir(path):
#         stats = os.stat(path + "/" + file)
#         filesize = stats[6]
#         isdir = stats[0] & 0x4000
 
#         if filesize < 1000:
#             sizestr = str(filesize) + " by"
#         elif filesize < 1000000:
#             sizestr = "%0.1f KB" % (filesize / 1000)
#         else:
#             sizestr = "%0.1f MB" % (filesize / 1000000)
 
#         prettyprintname = ""
#         for _ in range(tabs):
#             prettyprintname += "   "
#         prettyprintname += file
#         if isdir:
#             prettyprintname += "/"
#         print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

#         if isdir:
#             printDirectoryHelper(path + "/" + file, tabs + 1)

# def printDirectory():
#     print("Files on filesystem:")
#     print("====================")
#     printDirectoryHelper("/sd")

# def delFile(path):
#     #path is: "/sd/filenamehere"
#     os.remove(path)

# def writeFile(path, content):
#     #eg. path is: "/sd/t.txt"
#     with open(path, "a") as f:
#         # f.write(str(temp_c)+"#"+str(temp_f)+"\n")
#         f.write(content)

# while True:
#     if buttonA.value:  # button is pushed
#         #heartbeatPulse(heartBeat.value)
#         heartbeatCount(heartBeat.value)
#     elif buttonB.value:
#         temperature()




















# import time, board, digitalio, neopixel, adafruit_thermistor, busio, os, adafruit_sdcard, storage
# from analogio import AnalogIn

# #show heartbeat
# led = digitalio.DigitalInOut(board.D13)
# led.direction = digitalio.Direction.OUTPUT

# #start counting
# buttonA = digitalio.DigitalInOut(board.BUTTON_A)
# buttonA.direction = digitalio.Direction.INPUT
# buttonA.pull = digitalio.Pull.DOWN

# #start logging
# buttonB = digitalio.DigitalInOut(board.BUTTON_B)
# buttonB.direction = digitalio.Direction.INPUT
# buttonB.pull = digitalio.Pull.DOWN

# #show counting time
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01)

# # resistor = 10000
# # resistance = 10000
# # nominal_temp = 25
# # b_coefficient = 3950
# # adafruit_thermistor.Thermistor(pin, series_resistor, nominal_resistance, nominal_temperature, b_coefficient, *, high_side=True)
# thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

# # spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# # cs = digitalio.DigitalInOut(board.SCL)
# # sdcard = adafruit_sdcard.SDCard(spi, cs)
# # vfs = storage.VfsFat(sdcard)
# # storage.mount(vfs, "/sd")

# heartBeat = AnalogIn(board.A5)
# # convert from arduino to int(550/1024*65535) = 35199
# threshold = 35199

# def blink(pause=0.3, c=3):
#     # (0, 255, 0) green (0,0xBF,0x11)
#     for i in range(0, c):
#         pixels.fill((0, 255, 0))
#         pixels.show()
#         time.sleep(pause)
#         pixels.fill((0,0,0))
#         pixels.show()
#         time.sleep(pause)

# def heartbeatCount(hb, pause=0.1):
#     print("START!")
#     count, p = 0, 1
#     while count < 600:
#         if count % 60 == 0:
#             for i in range(0, p):
#                 pixels[i] = (255, 255, 255)
#             pixels.show()
#             p += 1
#         # hb = heartBeat.value
#         print(hb)
#         if hb >= 35199:
#             led.value = True
#         else:
#             led.value = False
#         time.sleep(pause)
#         # print(count)
#         count += 1
#     led.value = False
#     print("END!")
#     blink()

# # def heartbeatPulse(hb):
# #     # How many light readings per sample
# #     NUM_OVERSAMPLE = 10
# #     # How many samples we take to calculate 'average'
# #     NUM_SAMPLES = 20
# #     samples = [0] * NUM_SAMPLES
# #     for i in range(NUM_SAMPLES):
# #         # Take NUM_OVERSAMPLE number of readings really fast
# #         oversample = 0
# #         for s in range(NUM_OVERSAMPLE):
# #             oversample += float(hb)
# #         # and save the average from the oversamples
# #         samples[i] = oversample / NUM_OVERSAMPLE  # Find the average
 
# #         mean = sum(samples) / float(len(samples))  # take the average
# #         print(samples[i] - mean)  # 'center' the reading
# #         time.sleep(0.025)  # change to go faster/slower

# def temperature(pause=1):
#     c = thermistor.temperature
#     f = c * 9 / 5 + 32
#     print("Temperature is: %f C and %f F" % (c, f))
#     time.sleep(pause)

# def printDirectoryHelper(path, tabs=0):
#     for file in os.listdir(path):
#         stats = os.stat(path + "/" + file)
#         filesize = stats[6]
#         isdir = stats[0] & 0x4000
 
#         if filesize < 1000:
#             sizestr = str(filesize) + " by"
#         elif filesize < 1000000:
#             sizestr = "%0.1f KB" % (filesize / 1000)
#         else:
#             sizestr = "%0.1f MB" % (filesize / 1000000)
 
#         prettyprintname = ""
#         for _ in range(tabs):
#             prettyprintname += "   "
#         prettyprintname += file
#         if isdir:
#             prettyprintname += "/"
#         print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

#         if isdir:
#             printDirectoryHelper(path + "/" + file, tabs + 1)

# def printDirectory():
#     print("Files on filesystem:")
#     print("====================")
#     printDirectoryHelper("/sd")

# def delFile(path):
#     #path is: "/sd/filenamehere"
#     os.remove(path)

# def writeFile(path, content):
#     #eg. path is: "/sd/t.txt"
#     with open(path, "a") as f:
#         # f.write(str(temp_c)+"#"+str(temp_f)+"\n")
#         f.write(content)

# while True:
#     if buttonA.value:  # button is pushed
#         #heartbeatPulse(heartBeat.value)
#         heartbeatCount(heartBeat.value)
#     elif buttonB.value:
#         temperature()




























# import time, board, analogio

# alpha, period, change, oldValue, oldChange = 0.75, 20, 0.0, 0.0, 0.0

# while True:
#     rawValue = int(float(analogio.AnalogIn(board.A5).value) / 65535.0) * 1024
#     value = alpha * oldValue + (1-alpha) * rawValue
#     change = value - oldValue
#     print(rawValue)
#     print(change<0 and oldChange>0)
#     oldValue = value
#     oldChange = change
#     time.sleep(period/1000)














# import board, digitalio, time
# from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# from adafruit_hid.keycode import Keycode

# buttonA = digitalio.DigitalInOut(board.BUTTON_A)
# buttonA.direction = digitalio.Direction.INPUT
# buttonA.pull = digitalio.Pull.DOWN

# buttonB = digitalio.DigitalInOut(board.B)
# buttonB.direction = digitalio.Direction.INPUT
# buttonB.pull = digitalio.Pull.DOWN

# kbd = Keyboard()
# layout = KeyboardLayoutUS(kbd)
# words = "abcdefg"
# status = 0

# while True:
#     if buttonA.value and status == 0:  # button is pushed
#         for i in words:
#            # kbd.press(eval("Keycode."+chr(ord(i)-32)))
#            # kbd.release(eval("Keycode."+chr(ord(i)-32)))
#			  kbd.press(eval("Keycode."+i.upper()))
#             kbd.release(eval("Keycode."+i.upper()))
#         time.sleep(1)
#         status = 1
#     if buttonA.value and status == 1:
#         status = 0




























import board, digitalio, time, adafruit_sdcard, busio, storage, adafruit_thermistor, adafruit_lis3dh, neopixel, analogio, os

sw = digitalio.DigitalInOut(board.SLIDE_SWITCH)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

hb = analogio.AnalogIn(board.A5)

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.03)

lis3dh_i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(lis3dh_i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_8_G

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.SCL)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

def printDirectoryHelper(path, tabs=0):
    for file in os.listdir(path):
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000
 
        if filesize < 1000:
            sizestr = str(filesize) + " by"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)
 
        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

        if isdir:
            printDirectoryHelper(path + "/" + file, tabs + 1)

def printDirectory():
    print("Files on filesystem:")
    print("====================")
    printDirectoryHelper("/sd")

def temperature(pause=1):
    c = thermistor.temperature
    f = c * 9 / 5 + 32
    # print("Temperature is: %f C and %f F" % (c, f))
    time.sleep(pause)
    return dict(zip(["c", "f"], [c, f]))

def motion(pause=1):
    x, y, z = lis3dh.acceleration
    time.sleep(pause)
    return dict(zip(["x", "y", "z"], [x, y, z]))

def heartBeat(pause=1):
    return hb.value

def analysis():
    hbs = []
    for i in range(0,10):
        hbs.append(int(hb.value/65535*4096))
        time.sleep(0.02)
    return sum(sorted(hbs)[1:9])/8

def blink(pause=0.3, c=3, color=(0, 255, 0)):
    # (0, 255, 0) green (0,0xBF,0x11)
    for i in range(0, c):
        pixels.fill(color)
        pixels.show()
        time.sleep(pause)
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(pause)

# blink(pause=1, c=1) #ini finishes

dfilter, dmax, dmin, dmid = 0, 0, 0, 0
PULSE, PRE_PULSE = False, False
pulseCount = 0
IBI, BPM, SIG = 0, 0, 0
readData, preReadData = 0, 0
#发送给上位机的三个量 IBI: 相邻两个心跳的时间，BPM: 心率值， SIG: 脉象图的数值化表示
timeCount, firstTimeCount, secondTimeCount = 0, 0, 0
data = []

while True:
    if sw.value: #left is True
        # print(temperature())
        # print(motion())
        # blink(color=(255,0,0))
        # print(heartBeat.value)
        # print(heartBeat(0.2))
        preReadData = readData
        readData = analysis()
        if (readData - preReadData) < dfilter:
            data.append(readData)
        if len(data) >= 50:
            dmax = max(data)
            dmin = min(data)
            dmid = (dmax+dmin)/2
            dfilter = (dmax-dmin)/2
            data = []
        PRE_PULSE = PULSE
        PULSE = True if readData > dmid else False
        if PRE_PULSE == False and PULSE == True:
            pulseCount += 1
            pulseCount %= 2
            if pulseCount == 1:
                firstTimeCount = timeCount
            if pulseCount == 0:
                secondTimeCount = timeCount
                timeCount = 0
                if secondTimeCount > firstTimeCount:
                    IBI = (secondTimeCount - firstTimeCount) * 160
                    BPM = 60000 / IBI
                    if BPM > 200:
                        BPM = 200                 
                    if BPM < 30:
                        BPM = 30
            print("SIG = %d IBI = %d, BMP = %d\n\n" % (readData, IBI, BPM))
        timeCount += 1
        time.sleep(0.02)



















# <!DOCTYPE html>
# <html>
# <head>
# <title>CISC 340 Group 11</title>
# <meta http-equiv='content-type' content='text/html;charset=UTF-8' />
# <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=0' />
# <style>
#  html{
# 	-moz-osx-font-smoothing:grayscale; 
# 	-webkit-font-smoothing:antialiased; 
# 	text-rendering:optimizeLegibility; 
#  }

# body:before{
# 	content:'';
#  	position:fixed;
# 	top:-10px;
# 	left:0;
# 	width:100%;
# 	height:10px;
# 	-webkit-box-shadow:0px 0px 10px rgba(0,0,0,.8);
# 	-moz-box-shadow:0px 0px 10px rgba(0,0,0,.8);
# 	box-shadow:0px 0px 10px rgba(0,0,0,.8);
# 	z-index:100;
# }
# .calendar{table-layout:fixed;}
# caption{font-size:35px;}
# </style>

# <script>
# var xmlData=null;
# function newxmlData(){xmlData=window.XMLHttpRequest?new XMLHttpRequest():new ActiveXObject('Microsoft.XMLHttp');}
# function retData(){
# 	if(xmlData.readyState==4&&xmlData.status==200){
# 		var res=xmlData.responseText;
# 		if(res.length>0){
# 			var v=res.split('$');
# 			if (v.length==6){
# 				for(i=1;i<7;i++){
# 					document.getElementById(i).innerHTML=v[i];
# 				}
# 			}else{
# 				for(i=1;i<7;i++){
# 					document.getElementById(i).innerHTML='Loading...';
# 				}
# 			}
# 		}else{
# 			for(i=1;i<7;i++){
# 				document.getElementById(i).innerHTML='Loading...';
# 			}
# 		}
# 	}
# }

# function getData(){
# 	newxmlData();
# 	xmlData.onreadystatechange=retData;
# 	xmlData.open('POST','data',true);
# 	xmlData.send(null);
# }

# </script>

# </head><body>

# <table width='100%' border='1' class='calendar'>
# <caption>Data</caption>
# <tr>
# 	<th align='center'>Temperature</th>
# 	<th align='center'>Motion X</th>
# 	<th align='center'>Motion Y</th>
# 	<th align='center'>Motion Z</th>
# 	<th align='center'>IBI</th>
# 	<th align='center'>BPM</th>
# </tr>
# <tr>
# 	<td align='center' id=1>Loading...</td>
# 	<td align='center' id=2>Loading...</td>
# 	<td align='center' id=3>Loading...</td>
# 	<td align='center' id=4>Loading...</td>
# 	<td align='center' id=5>Loading...</td>
# 	<td align='center' id=6>Loading...</td>
# </tr>
# </table>
# <script>getData();</script>
# </body>
# </html>