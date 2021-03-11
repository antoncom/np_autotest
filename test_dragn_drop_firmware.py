from seleniumbase import BaseCase
import helium as hm


class ApplyFirmware(BaseCase):

    firmware_valid   =  True
    web_page_address =  "http://_USER_:_PASSWORD_@tst.alentis.ru:8040/update.html"
    firmware_path    =  "/home/anton/python_projects/np_autotest/data/"
    fw_fake_filename =  "[Pub] DKSF 70.7.4.R.npu" # required becase of bug in the drag-n-drop feature
    fw_real_filename =  "test_firmware4.npu"

    
    def test_1_DRAGN_DROP_FIRMWARE_VALID(self):
        # =================================== #
        hm.start_firefox(self.web_page_address, headless=True)
        browser = hm.get_driver()
        error_text = "Данный файл не содержит подходящую прошивку!"

        hm.drag_file(self.firmware_path + self.fw_fake_filename, to=browser.find_element_by_id("holder"))
        hm.drag_file(self.firmware_path + self.fw_real_filename, to=browser.find_element_by_id("holder"))

        error_message = '<span id="status_drop" class="alert">' + error_text + '</span>'
        ApplyFirmware.firmware_valid = error_message not in browser.page_source
        
        assert error_message not in browser.page_source, "Данный файл не содержит подходящую прошивку!"

    
    def test_2_FIRMWARE_LOADED(self):
        # ========================= #
        self.driver = hm.get_driver()
        if not ApplyFirmware.firmware_valid:
            self.skip("Skip test 2: Firmware file is invalid!")

        self.wait_for_exact_text_visible("test_firmware4.npu", selector="#dropname", timeout=10)
        self.click('#update', timeout=5)
        self.wait_for_exact_text_visible("Загрузка кода прошивки: 100%", selector="#status_fw", timeout=60)

        assert "Загрузка кода прошивки: 100%" in self.get_page_source()


    def test_3_FIRMWARE_CODEBASE_REPLACED(self):
        # ==================================== #
        if not ApplyFirmware.firmware_valid:
            self.skip("Skip test 3: Firmware file is invalid!")

        self.driver = hm.get_driver()
        self.wait_for_exact_text_visible("Переход на новый код прошивки успешно завершён", selector="#status_reboot", timeout=60)

        assert "Переход на новый код прошивки успешно завершён" in self.get_page_source()


    def test_4_NEW_WEBINTERFACE_PAGES_LOADED(self):
        # ======================================= #
        if not ApplyFirmware.firmware_valid:
            self.skip("Skip test 4: Firmware file is invalid!")

        self.driver = hm.get_driver()
        self.wait_for_exact_text_visible("Загрузка новых страниц вебинтерфейса: 100%", selector="#status_res", timeout=60)

        assert "Загрузка новых страниц вебинтерфейса: 100%" in self.get_page_source()


    def test_5_FIRMWARE_APPLIED(self):
        # ========================== #
        if not ApplyFirmware.firmware_valid:
            self.skip("Skip test 5: Firmware file is invalid!")

        self.driver = hm.get_driver()
        self.wait_for_exact_text_visible("Обновление прошивки успешно завершено!", selector="#status_final", timeout=60)

        assert "Обновление прошивки успешно завершено!" in self.get_page_source()
        self.driver.close()
