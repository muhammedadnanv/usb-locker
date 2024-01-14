Certainly! Below is a technical write-up for the USB Locker project available at https://github.com/muhammedadnanv/usb-locker.git.

---

# USB Locker

## Overview

USB Locker is a simple Python script that allows users to control access to USB storage devices on a Windows system. The script uses the `pywinusb` library to monitor USB devices and can either allow or block them based on user configuration.

## Features

- **Device Monitoring**: Monitors connected USB devices in real-time.
- **Allowlisting**: Users can specify allowed USB devices, preventing unauthorized devices from mounting.
- **Blocking Mechanism**: If a USB device is not in the allowlist, it can be blocked from accessing the system.

## Prerequisites

- **Python**: Ensure that Python is installed on the system.
- **Dependencies**: Install the required dependencies using `pip install -r requirements.txt`.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/muhammedadnanv/usb-locker.git
   cd usb-locker
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**

   ```bash
   python usb_locker.py
   ```

   The script will start monitoring for USB devices and block any USB storage devices not in the allowlist.

4. **Stop Monitoring:**

   Press Enter to stop monitoring.

## Configuration

- Edit the script to customize the list of allowed devices and adjust the blocking mechanism as needed.

## Considerations

- This script is specific to Windows and relies on the `pywinusb` library.
- Blocking USB devices may have system-wide consequences, use with caution.
- Always test in a controlled environment to understand the impact.

## Acknowledgments

This project is based on the `pywinusb` library and serves as an educational example for controlling USB device access in a Windows environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Muhammed Adnan** - [GitHub](https://github.com/muhammedadnanv)

---

Feel free to customize this technical write-up based on additional details or specific instructions from the project's documentation.
