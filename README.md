# razerPython
A library wrapper for controlling your razer devices easily with python
Coded by me and my friend (https://github.com/pineapplefan1234YT)[PineappleFan]

# Setup
At the moment, devices are stored in a dictionary in the format {"friendlyname": <Device Object>, etc.}<br>
You can set the friendlynames to whatever you want, as that is the name you will use to apply effects and such.

Then:
- Update the for loop on line 10 with your devices
- Update your list of friendly devices on line 28 to match your friendlynames

# Apply
**razer.apply(colour, effect, devices)**<br><br>
**colour**
- a hexadecimal code in the exact format `"FFFFFF"`<br>

**effect**
- currently truly supported: "static", sets device to one whole colour<br>

**devices**
- choose which devices from your dictionary to apply i.e \["kbd", "mouse",]
- it must be the devices _friendlyname_
- leave blank to choose all devices

**example**<br>
razer.apply("FFFFFF", "static", ["kbd", "mouse"])

# Test.py
Run test.py as an example
