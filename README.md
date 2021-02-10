# razerPython
A library wrapper for controlling your razer devices easily with python
<br>
# Setup
At the moment, devices are stored in a dictionary in the format {"friendlyname": <Device Object>, etc.}<br>
You can set the friendlynames to whatever you want, as that is the name you will use to apply effects and such.
<br>
Then:
- Update the for loop on line 10 with your devices
- Update your list of friendly devices on line 28 to match your friendlynames
<br>
# Apply
**razer.apply(colour, effect, devices)**
**colour**<br>
- a hexadecimal code in the exact format `"FFFFFF"`
**effect**<br>
- currently truly supported: "static", sets device to one whole colour
**devices**<br>
- choose which devices from your dictionary to apply i.e \["kbd", "mouse",]
- it must be the devices _friendlyname_
- leave blank to choose all devices
<br>
**example**<br>
razer.apply("FFFFFF", "static", ["kbd", "mouse"])
<br>
# Test.py
Run test.py as an example
