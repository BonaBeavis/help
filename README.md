- Laptop password: helpyourself

## Quick Start

1. Go to `Settings` -> `Wi-Fi`
2. Press three dots in the upper right corner and select `Turn On Wi-Fi Hotspot...`
3. Open Firefox and check with bookmarks `Outlet A` and `Outlet B`, if they have already connected to the hotspot. If not WAIT.
4. Open `help` folder on the desktop.
5. Right click inside folder and select `Open in Terminal`.
6. Type: `./help.py` and press enter.

## Troubleshooting

Do this if the outlets do not connect to the laptop's hotspot:

### Create Hotspot on Laptop

1. Go to `Settings` -> `Wi-Fi`
2. Press three dots in the upper right corner and select `Turn On Wi-Fi Hotspot...`
3. ```txt
   Network Name: help
   Password: helpyourself
   ```

## Setup Outlets

You have to do this for each outlet!

1. Press outlet switch four times until LED blinks.
2. Connect with your mobile phone to the `delock-XXXX` network.
3. If the Hotspot Login window appears, tell the outlet to which network it should connect:
    ```txt
    WLAN 1 - SSID (): help
    WLAN 1 - Password: helpyourself
    ```
4. If the Hotspot Login window does not appear open Browser and enter URI:
    1. Outlet A: http://delock-0077.local/
    2. Outlet B: http://delock-2592.local/
