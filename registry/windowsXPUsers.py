from __future__ import unicode_literals
from registry.reg import _Reg


class WindowsXPUserReg(_Reg):
    def __init__(self, params):
        _Reg.__init__(self, params)
        _Reg.init_win_xp(self)

    def csv_open_save_mru(self):
        super(WindowsXPUserReg, self)._csv_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU")

    def csv_user_assist(self):
        super(WindowsXPUserReg, self)._csv_user_assist(-6, False)

    def json_open_save_mru(self):
        super(WindowsXPUserReg, self)._json_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU")

    def json_user_assist(self):
        super(WindowsXPUserReg, self)._json_user_assist(-6, False)

    def csv_hwp_mru(self):
        super(WindowsXPUserReg, self)._csv_hwp_mru(
            r"Software\\HNC\\Hwp\\9.0\\HwpFrame_KOR\\RecentFile")

    def json_hwp_mru(self):
        super(WindowsXPUserReg, self)._json_hwp_mru(
            r"Software\\HNC\\Hwp\\9.0\\HwpFrame_KOR\\RecentFile")