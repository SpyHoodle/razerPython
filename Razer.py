import openrazer.client as rclient

class Razer:
    def __init__(self):

        dmanager = rclient.DeviceManager()
        dlist = [device for device in dmanager.devices]
        self.ddict = {}

        for device in dlist:
            if device.name == "Razer Goliathus":
                device.brightness = 100
                self.ddict["mat"] = device
            elif device.name == "Razer Chroma HDK":
                device.brightness = 100
                self.ddict["monitor"] = device
            elif device.name == "Razer Huntsman":
                device.brightness = 100
                self.ddict["kbd"] = device
            elif device.name == "Razer Base Station Chroma":
                device.brightness = 100
                self.ddict["stand"] = device
            elif device.name == "Razer Viper Mini":
                self.ddict["mouse"] = device
            elif device.name == "Razer Kraken 7.1 V2":
                self.ddict["headset"] = device

    def apply(self, col, effect, devices=["kbd", "mouse", "mat", "stand", "headset", "monitor"]):
        self._apply(col, effect, devices)

    def _applydevice(self, device, effect, r, g, b):
        if device == "mouse":
            if effect == "static":
                self.ddict[device].fx.misc.logo.static(r, g, b)
            elif effect == "reactive":
                self.ddict[device].fx.misc.logo.reactive(r, g, b, time=rclient.constants.REACTIVE_500MS)
        elif device == "kbd":
            if effect == "static":
                self.ddict[device].fx.static(r, g, b)
            elif effect == "reactive":
                self.ddict[device].fx.reactive(r, g, b, time=rclient.constants.REACTIVE_1000MS)
            elif effect == "starlight":
                self.ddict[device].fx.starlight(r, g, b)
        else:
            self.ddict[device].fx.static(r, g, b)

    def _apply(self, col, effect, devices):
        r, g, b = [col[i:i+2] for i in range(0, len(col), 2)]
        r, g, b = int(r, 16), int(g, 16), int(b, 16)
        for device in devices:
            print(f"[APPLY] {self.ddict[device].name} to R:{r} G:{g} B:{b}")
            self._applydevice(device, effect, r, g, b)
        print("-"*25)
