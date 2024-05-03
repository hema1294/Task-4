#Python program to convert UML diagram into a python class and its methods
# Given UML diagram - https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md 

#Part - A

class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1  # Default channel
        self.volume = 50  # Default volume
        self.on = False  # TV is initially turned off

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
    
# Create a TV object
my_tv = TV("Sony")

# Set some properties
my_tv.set_channel(8)
my_tv.increase_volume()

# Get the status
print(my_tv.status())  # Output: Sony at channel 8, volume 51

# Part - B

class LEDTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Wide viewing angle"

    def backlight(self):
        return "LED backlight"

    def display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Narrow viewing angle"

    def backlight(self):
        return "Plasma backlight"

    def display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"