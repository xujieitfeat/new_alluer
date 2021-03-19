import pytest
import yaml

from base.base_analyze import analyze_data
from page.contact_list_page import ContactListPage
from page.edit_contact_page import EditContactPage

from appium import webdriver



class TestContact:

    def setup(self):
        # 创建一个字典，包装相应的启动参数
        desired_caps = dict()
        # 需要连接的手机的平台(不限制大小写)
        desired_caps['platformName'] = 'Android'
        # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
        desired_caps['platformVersion'] = '5.1'
        # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # 需要启动的程序的包名
        desired_caps['appPackage'] = 'com.android.contacts'
        # 需要启动的程序的界面名
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        # 告诉系统不需要重置
        desired_caps['noReset'] = True
        # 解决中文问题
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 连接appium服务器
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.contact_list_page = ContactListPage(self.driver)
        self.edit_contact_page = EditContactPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("contact_data.yaml", "test_add_contact"))
    def test_add_contact(self, args):

        name = args["name"]
        email = args["email"]

        self.contact_list_page.click_add_contact()
        self.edit_contact_page.input_name(name)
        self.edit_contact_page.input_email(email)




    # @pytest.mark.parametrize("args", analyze_data("contact_data.yaml", "test_add_contact"))
    # def test_add_contact(self, args):
    #
    #     name = args["name"]
    #     phone = args["phone"]
    #
    #     print(name)
    #     print(phone)


