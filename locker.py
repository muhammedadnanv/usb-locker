import time
from pywinusb import hid

class USBLocker:
    def __init__(self):
        self.allowed_devices = set()
        self.monitor_thread = None

    def allow_device(self, device):
        print(f"Allowing device: {device.product_name}")
        self.allowed_devices.add(device)

    def block_device(self, device):
        print(f"Blocking device: {device.product_name}")
        # You can implement device blocking logic here (e.g., disable the device)

    def on_device_arrival(self, event):
        device = event.device
        if device not in self.allowed_devices:
            self.block_device(device)

    def on_device_removal(self, event):
        pass

    def monitor_usb(self):
        filters = hid.HidDeviceFilter()

        while True:
            for device in filters.get_devices():
                if device not in self.allowed_devices:
                    self.block_device(device)

            time.sleep(5)

    def start_monitoring(self):
        hid.HidDeviceMonitor.start()
        monitor_thread = threading.Thread(target=self.monitor_usb)
        monitor_thread.daemon = True
        monitor_thread.start()
        self.monitor_thread = monitor_thread

if __name__ == "__main__":
    usb_locker = USBLocker()
    usb_locker.start_monitoring()
    input("Press Enter to stop monitoring...\n")
