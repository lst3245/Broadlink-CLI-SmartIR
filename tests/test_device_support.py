import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

import broadlink
from helpers import isSupportedRemote


def _make_device(cls, devtype: int, model: str):
    return cls(('192.168.9.55', 80), mac=bytes(6), devtype=devtype, model=model)


class DeviceSupportTest(unittest.TestCase):
    def test_rm_mini_3_classic_is_supported(self):
        device = _make_device(broadlink.rmmini, 0x2737, 'RM mini 3')
        self.assertTrue(isSupportedRemote(device))

    def test_rm_mini_3_new_firmware_is_supported(self):
        device = _make_device(broadlink.rmminib, 0x5F36, 'RM mini 3')
        self.assertTrue(isSupportedRemote(device))

    def test_rm4_devices_remain_supported(self):
        rm4mini = _make_device(broadlink.rm4mini, 0x51DA, 'RM4 mini')
        rm4pro = _make_device(broadlink.rm4pro, 0x6026, 'RM4 pro')
        self.assertTrue(isSupportedRemote(rm4mini))
        self.assertTrue(isSupportedRemote(rm4pro))

    def test_non_remote_device_is_rejected(self):
        device = _make_device(broadlink.sp2, 0x2711, 'SP2')
        self.assertFalse(isSupportedRemote(device))


if __name__ == '__main__':
    unittest.main()
