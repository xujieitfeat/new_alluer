import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):

    # 添加联系人的按钮
    add_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    # 搜索的按钮
    search_button = By.ID, "com.android.contacts:id/menu_search"

    # 搜索输入框
    search_edit_text = By.ID, "com.android.contacts:id/search_view"

    # 点击 添加联系人
    @allure.step(title='联系人列表 - 点击添加联系人')
    def click_add_contact(self):
        self.click(self.add_contact_button)

    # 点击 搜索
    @allure.step(title='联系人列表 - 点击搜索')
    def click_search(self):
        self.click(self.search_button)

    # 输入 搜索
    @allure.step(title='联系人列表 - 输入搜索')
    def input_search(self, text):
        self.input(self.search_edit_text, text)
        allure.attach('A text attacment in module scope finalizer', 'blah blah blah blah',
                      allure.attachment_type.TEXT)
        # self.driver.get_screenshot_as_file("./screen/xx.png")
        # allure.attach.file('./screen/xx.png', attachment_type=allure.attachment_type.PNG)