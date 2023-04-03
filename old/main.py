import random
import time

from selenium.webdriver.common.by import By
from selenium import webdriver


class Post_form(object):
    def __init__(self):
        self.__driver = webdriver.Chrome()

    def get_url(self):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLScOrRfLRBm3b31xFklnuwBiRCe9NbAmHAKC5qsOFY4-41RNYw/viewform'
        self.__driver.get(url)
        self.__driver.maximize_window()
        self.__driver.implicitly_wait(3)

    def _one_page(self):
        self.__driver.find_element(By.XPATH, '//*[@id="i7"]').click()
        self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

    def _two_page(self):
        self.__driver.find_element(By.XPATH, '//*[@id="i5"]').click()
        self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()

    def _three_page(self):
        one_list = self.__driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]')
        list_post = one_list.find_elements(By.CLASS_NAME, 'eBFwI')
        temp_random = random.randint(0, len(list_post) - 1)
        list_post[temp_random].click()
        temp_random = random.randint(0, len(list_post) - 1)
        list_post[temp_random].click()

        self.__driver.find_element(By.XPATH, '//*[@id="i31"]').click()

        self.__driver.find_element(By.XPATH, '//*[@id="i44"]').click()

        two_list = self.__driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]')

        for i in range(0, random.randint(1, 3)):
            list_post_two = two_list.find_elements(By.CLASS_NAME, 'eBFwI')
            temp_random = random.randint(0, len(list_post_two) - 1)
            if temp_random != 1:
                list_post_two[temp_random].click()
                time.sleep(0.3)
        temp_rando_1 = random.randint(0, 1)
        if temp_rando_1 == 0:
            self.__driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div').click()
        else:
            self.__driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div').click()
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div').click()
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]').click()
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]').click()
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div').click()

        self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()

    def _four_page(self):
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]').click()

        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]').click()
        time.sleep(0.3)
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[5]').click()
        # two_list = self.__driver.find_element(By.XPATH,
        #                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]')

        # for i in range(0,random.randint(1,3)):
        #    list_post_two = two_list.find_elements(By.CLASS_NAME, 'eBFwI')
        #   temp_random = random.randint(0, len(list_post_two) - 1)
        #   list_post_two[temp_random].click()
        #   time.sleep(0.3)

        # two_list = self.__driver.find_element(By.XPATH,
        #                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]')
        #
        # for i in range(0, random.randint(1, 4)):
        #    try:
        #        list_post_two = two_list.find_elements(By.CLASS_NAME, 'eBFwI')
        #        temp_random = random.randint(0, len(list_post_two) - 1)
        #        list_post_two[temp_random].click()
        #       time.sleep(0.3)
        #    except Exception as E:
        #      print(E)

        for i in range(2, 16, 2):
            try:
                temp_array = self.__driver.find_element(By.XPATH,
                                                        f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[{i}]/span')
                temp_array.find_elements(By.CLASS_NAME, 'V4d7Ke')[random.randint(1, 2)].click()
                time.sleep(0.3)
            except Exception as E:
                print(E)

        tem_d = random.randint(0, 1)
        if tem_d == 0:
            self.__driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div').click()
        else:
            self.__driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div').click()
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div').click()
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label/div').click()

        for i in range(2, 14, 2):
            try:
                temp_array = self.__driver.find_element(By.XPATH,
                                                        f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[{i}]/span')
                temp_array.find_elements(By.CLASS_NAME, 'V4d7Ke')[random.randint(1, 2)].click()
            except Exception as E:
                print(E)

        self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()

    def _five_page(self):
        self.__driver.find_element(By.XPATH, '//*[@id="i5"]').click()

        with open('text.txt', 'r+', encoding='utf-8') as file:
            array_text = [i for i in file.readlines()]
        send_mess = array_text[random.randint(0, len(array_text) - 1)]
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(
            send_mess)
        self.__driver.find_element(By.XPATH, '//*[@id="i19"]').click()
        self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()

    def _six_page(self):
        count = random.randint(0, 1)
        if count == 0:
            self.__driver.find_element(By.XPATH, '//*[@id="i5"]').click()
        else:
            self.__driver.find_element(By.XPATH, '//*[@id="i8"]').click()

        tem_array = self.__driver.find_element(By.XPATH,
                                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div')
        list_post_two = tem_array.find_elements(By.CLASS_NAME, 'YEVVod')
        temp_random = random.randint(0, len(list_post_two) - 2)
        list_post_two[temp_random].click()

        tem_array = self.__driver.find_element(By.XPATH,
                                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div')
        list_post_two = tem_array.find_elements(By.CLASS_NAME, 'YEVVod')
        temp_random = random.randint(0, len(list_post_two) - 1)
        list_post_two[temp_random].click()

        self.__driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()

    def __start__(self):
        self.get_url()
        self._one_page()
        self._two_page()
        self._three_page()
        self._four_page()

        self._five_page()
        self._six_page()


if __name__ == '__main__':
    # 10 + 120
    for i in range(0, 40):
        test_class = Post_form()
        test_class.__start__()
        print(i)
