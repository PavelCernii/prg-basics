class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = False
        self.apps = []
        
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"Installed {app_name} on {self.brand} {self.model}.")

    def use_app(self, app_name):
        if app_name in self.apps and self.is_on:
            print(f"Using {app_name} on {self.brand} {self.model}.")
        elif not self.is_on:
            print(f"Cannot use {app_name}. The phone is OFF.")
        else:
            print(f"{app_name} is not installed.")

    def display_info(self):
        print(f"Smartphone Info:\nBrand: {self.brand}\nModel: {self.model}\nBattery Level: {self.battery_level}%\nInstalled Apps: {', '.join(self.apps) if self.apps else 'No apps installed.'}")

my_phone = Smartphone("Samsung", "Galaxy S21", 85)

my_phone.power_on()
my_phone.install_app("Instagram")
my_phone.install_app("Spotify")
my_phone.use_app("Instagram")
my_phone.display_info()
