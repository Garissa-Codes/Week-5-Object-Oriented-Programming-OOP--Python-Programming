class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self._brand = brand
        self._model = model
        self._battery_percentage = battery_percentage

    def make_call(self, number):
        if self._battery_percentage > 0:
            print(f"Calling {number} from {self._brand} {self._model}...")
            self._battery_percentage -= 1
        else:
            print("Battery too low to make a call.")

    def send_message(self, number, message):
        if self._battery_percentage > 0:
            print(f"Sending message to {number}: {message}")
            self._battery_percentage -= 1
        else:
            print("Battery too low to send a message.")

    def charge_battery(self, amount):
        if amount < 0:
            raise ValueError("Charge amount must be positive")
        self._battery_percentage = min(self._battery_percentage + amount, 100)
        print(f"Battery charged to {self._battery_percentage}%.")

    # Encapsulation with getter methods
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_battery_percentage(self):
        return self._battery_percentage

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_percentage, performance_mode):
        super().__init__(brand, model, battery_percentage)
        self._performance_mode = performance_mode

    def enable_performance_mode(self):
        if self._performance_mode:
            print(f"Performance mode enabled on {self._brand} {self._model}.")
        else:
            print(f"{self._brand} {self._model} does not support performance mode.")

    # Polymorphism by overriding make_call method
    def make_call(self, number):
        if self._performance_mode:
            print(f"Calling {number} in performance mode from {self._brand} {self._model}...")
        else:
            super().make_call(number)

# Example usage
phone = Smartphone("Xiaomi", "X100", 50)
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")
phone.charge_battery(30)

gaming_phone = GamingSmartphone("GamingBrand", "Xiaomi", 70, True)
gaming_phone.enable_performance_mode()
gaming_phone.make_call("987-654-3210")