#!/usr/bin/env python -u
if __name__ == '__main__':
    import subprocess
    import time

    import notify2
    import psutil

    notify2.init('Thermald checker')
    while True:
        last_clocks = []
        last_temps = []
        reload_thermald = False

        temps = psutil.sensors_temperatures()
        for coreTemps in temps['coretemp']:
            last_temps.append(round(coreTemps.current))

        for core in psutil.cpu_freq(True):
            current =round(core.current/1000, 1)
            last_clocks.append(current)

        if (all(i <= 1.0 for i in last_clocks) and all(i <= 70 for i in last_temps)):
            reload_thermald = True

        if (reload_thermald == True):
            call = ['systemctl', 'reload', 'thermald']
            print('--- Temps ---')
            print(last_temps)
            print('------')
            print('--- Clocks ---')
            print(last_clocks)
            print('------')
            print('reload thermald!')
            notify2.Notification('Thermald Checker', 'We should reload Thermald!').show()
            subprocess.check_call(call)
        time.sleep(5)
