# Designing Class

class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def make_call(self, number):
        if self.battery_percentage > 0:
            print(f"Calling {number} from {self.brand} {self.model}...")
            self.battery_percentage -= 1
        else:
            print("Battery too low to make a call.")

    def send_message(self, number, message):
        if self.battery_percentage > 0:
            print(f"Sending message to {number}: {message}")
            self.battery_percentage -= 1
        else:
            print("Battery too low to send a message.")

    def charge_battery(self, amount):
        self.battery_percentage = min(self.battery_percentage + amount, 100)
        print(f"Battery charged to {self.battery_percentage}%.")

# Subclass demonstrating inheritance
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_percentage, performance_mode):
        super().__init__(brand, model, battery_percentage)
        self.performance_mode = performance_mode

    def enable_performance_mode(self):
        if self.performance_mode:
            print(f"Performance mode enabled on {self.brand} {self.model}.")
        else:
            print(f"{self.brand} {self.model} does not support performance mode.")

# Example usage
phone = Smartphone("Xiaomi", "X100", 50)
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")
phone.charge_battery(30)

gaming_phone = GamingSmartphone("GamingBrand", "Xiaomi", 70, True)
gaming_phone.enable_performance_mode()
gaming_phone.make_call("987-654-3210")
