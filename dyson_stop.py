from libpurecoollink.dyson import DysonAccount
from libpurecoollink.const import FanSpeed, FanMode, NightMode, Oscillation, \
    FanState, StandbyMonitoring, QualityTarget, ResetFilter, HeatMode, \
    FocusMode, HeatTarget
import urllib3
from config import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
dyson_account = DysonAccount(config["account"], config["password"], config["language"])
logged = dyson_account.login()

if logged:
    print("login successfully");
    devices = dyson_account.devices()
    connected = devices[0].connect("192.168.1.101")

    if connected:
        print("connect successfully")
        devices[0].set_configuration(fan_mode=FanMode.OFF)
        devices[0].disconnect()