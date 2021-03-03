from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # 打开页面需要登录，使用cookies
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 带有登录信息的cookies
        cookies = [{'domain': '.qq.com', 'expiry': 1614742732, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853863075669'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853863075669'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325131412053'}, {'domain': '.qq.com', 'expiry': 1614829072, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1120758946.1614648886'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'qmijFDH1ELV2tRvVwaEZIkCLo6BsRrJYaazkrekokbUQY2_EXi-BAX-soIFlLtu6'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6397453'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614742611'}, {'domain': '.qq.com', 'expiry': 1645594643, 'httpOnly': False, 'name': 'ied_qq', 'path': '/', 'secure': False, 'value': 'o1308598575'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '33654285222134846'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'mGRKRBlNzsJDrF0_ATWDv2gypmNCjwF4pWKxVOR2Bliauw1pawsRPeYFCXpjfxACtKcAZFtJDqS_9fEwQq2hurAfAfambnomMXlFuhMbUgeC-4gUb8iMeLQn_RiPcB9P9QiO3aAE-Qnv3UZYpHPXB7FWQaAxiHgvWWrpMVqOaBeZ89i9wKkmOKm-0JLravtzsuptlDD-IqODDgZOK5TzTaBNFGKjIP88ACwnFf3Miy_9tFqd-w0aQ91jnZSJjrI280F6x0cPM5WTAMiFJhIWzw'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646278611, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614648885,1614738090,1614738250,1614742538'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614769624, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1lvmr9l'}, {'domain': '.qq.com', 'expiry': 1645594643, 'httpOnly': False, 'name': 'uin_cookie', 'path': '/', 'secure': False, 'value': 'o1308598575'}, {'domain': '.qq.com', 'expiry': 1644402325, 'httpOnly': False, 'name': 'LW_uid', 'path': '/', 'secure': False, 'value': 'h1L6g1n2b8B6w6x3H2W5G0C5c6'}, {'domain': '.qq.com', 'expiry': 1644402325, 'httpOnly': False, 'name': 'LW_sid', 'path': '/', 'secure': False, 'value': 'k1B6g1J2a8a6I6z3t2q560J5L5'}, {'domain': '.qq.com', 'expiry': 1616650639, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1308598575'}, {'domain': '.qq.com', 'expiry': 1677814672, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1497674799.1613537238'}, {'domain': '.work.weixin.qq.com', 'expiry': 1617334715, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1642314336, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'h1P6U1G0p727u8d323x6x8n5m4'}, {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'L16BBUYLdA'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '209070230'}, {'domain': '.qq.com', 'expiry': 2147483653, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'fde4dab0bc71ebb342cb9e808c298af00930beb4131838a4b1323f56f760ca89'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645073217, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}]
        # 将带有登录信息的cookie加入到登陆的页面中

        for cookie in cookies:
            # expiry 生成时有时会生成浮点数，cookie不支持浮点数，所以删除
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开页面（已带有cookie）
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)

    def test_importcontact(self):
        # 打开页面需要登录，使用cookies
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 带有登录信息的cookies
        cookies = [
            {'domain': '.qq.com', 'expiry': 1614742732, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853863075669'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853863075669'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325131412053'},
            {'domain': '.qq.com', 'expiry': 1614829072, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1120758946.1614648886'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'qmijFDH1ELV2tRvVwaEZIkCLo6BsRrJYaazkrekokbUQY2_EXi-BAX-soIFlLtu6'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6397453'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1614742611'},
            {'domain': '.qq.com', 'expiry': 1645594643, 'httpOnly': False, 'name': 'ied_qq', 'path': '/',
             'secure': False, 'value': 'o1308598575'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '33654285222134846'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'mGRKRBlNzsJDrF0_ATWDv2gypmNCjwF4pWKxVOR2Bliauw1pawsRPeYFCXpjfxACtKcAZFtJDqS_9fEwQq2hurAfAfambnomMXlFuhMbUgeC-4gUb8iMeLQn_RiPcB9P9QiO3aAE-Qnv3UZYpHPXB7FWQaAxiHgvWWrpMVqOaBeZ89i9wKkmOKm-0JLravtzsuptlDD-IqODDgZOK5TzTaBNFGKjIP88ACwnFf3Miy_9tFqd-w0aQ91jnZSJjrI280F6x0cPM5WTAMiFJhIWzw'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1646278611, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1614648885,1614738090,1614738250,1614742538'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1614769624, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1lvmr9l'},
            {'domain': '.qq.com', 'expiry': 1645594643, 'httpOnly': False, 'name': 'uin_cookie', 'path': '/',
             'secure': False, 'value': 'o1308598575'},
            {'domain': '.qq.com', 'expiry': 1644402325, 'httpOnly': False, 'name': 'LW_uid', 'path': '/',
             'secure': False, 'value': 'h1L6g1n2b8B6w6x3H2W5G0C5c6'},
            {'domain': '.qq.com', 'expiry': 1644402325, 'httpOnly': False, 'name': 'LW_sid', 'path': '/',
             'secure': False, 'value': 'k1B6g1J2a8a6I6z3t2q560J5L5'},
            {'domain': '.qq.com', 'expiry': 1616650639, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '1308598575'},
            {'domain': '.qq.com', 'expiry': 1677814672, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1497674799.1613537238'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1617334715, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1642314336, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'h1P6U1G0p727u8d323x6x8n5m4'},
            {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'L16BBUYLdA'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'sameSite': 'None', 'secure': True, 'value': '209070230'},
            {'domain': '.qq.com', 'expiry': 2147483653, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'fde4dab0bc71ebb342cb9e808c298af00930beb4131838a4b1323f56f760ca89'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1645073217, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]
        # 将带有登录信息的cookie加入到登陆的页面中

        for cookie in cookies:
            # expiry 生成时有时会生成浮点数，cookie不支持浮点数，所以删除
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开页面（已带有cookie）
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击导入通讯录
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # 点击上传文件
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/a/input').send_keys("D:\Pycharm\python_cookiehomework\mydata.xlsx")
        sleep(2)
        # 获取文件名并断言
        assert "mydata.xlsx" == self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]').text