# Thermald Checker

I wrote this python script to fix an issue I had with my P14s Gen2i (equipped with an Intel i7 1165G7). After coldboots and sleep, thermald would run in erratic ways (throttling down to 0.4Ghz despite the temps being around 65C) which required me to restart thermald to return the clocks back to normal.

This script checks the temps and clocks of the cpu every 5 seconds. If the clocks are under 1GHz, and the temps under 70C, thermald will be restarted.

## Prerequisites

Install the required dependencies by running:

```bash
sudo apt install libsystemd-dev
pip3 install -r requirements.txt
```

In case of the P14s, `/etc/systemd/system/thermald.service.d/override.conf` should look like this, so thermald runs despite lapmode:

```bash
[Service]
ExecStart=
ExecStart=/usr/sbin/thermald --systemd --dbus-enable --ignore-cpuid-check

```
Copy thermaldChecker.service to `/etc/systemd/system/`

## Usage

Enable the service by typing this into a terminal:

```bash
sudo systemctl enable thermaldChecker.service
sudo systemctl start thermaldChecker.service
```

You can check the status by typing this into a terminal:

```bash
sudo systemctl status thermaldChecker.service
or
journalctl -xeu thermaldChecker
```
