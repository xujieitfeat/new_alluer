import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditContactPage(BaseAction):

    # 姓名输入框
    name_edit_text = By.XPATH, "//*[@text='姓名']"
    # 电话输入框
    phone_edit_text = By.XPATH, "//*[@text='电话']"
    # 电子邮件输入框
    email_edit_text = By.XPATH, "//*[@text='电子邮件']"


    # 输入 姓名
    @allure.step(title='编辑联系人 - 输入姓名')
    def input_name(self, text):
        a = [1, 2]
        print(a[3])
        self.input(self.name_edit_text, text)

    # 输入 电话
    @allure.step(title='编辑联系人 - 输入电话')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    # 输入 电子邮件
    @allure.step(title='编辑联系人 - 输入邮箱')
    def input_email(self, text):
        self.input(self.email_edit_text, text)

