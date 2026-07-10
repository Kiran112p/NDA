from selenium.webdriver.common.by import By

# Locators
username = (By.ID, "username")
password = (By.ID, "password")
login_btn = (By.CLASS_NAME, "btn-login")

#device managmenet locaters
navi_dm_page=(By.XPATH, '//*[@href="#device-management"]')
d_name_id=(By.ID,"deviceName")
d_ip_id=(By.ID,"deviceIp")
d_uname_id=(By.ID,"deviceUname")
d_pwd_id=(By.ID,"devicePassword")
d_type_id=(By.ID,"deviceType")
d_version_id=(By.ID,"deviceVersion")
d_host_id=(By.ID,"deviceHostname")
d_proto_id=(By.ID,"deviceProtocol")
save_button=(By.XPATH,'(//button[@class="btn-primary"])[4]')

    #test device managment page locators
device_name= (By.XPATH, "//td[text()='ROUTER_NCS_540']")
device_ip= (By.XPATH, "//td[text()='192.168.1.100']")
user_name= (By.XPATH, "//td[text()='Kiran112']")
device_model= (By.XPATH, "//td[text()='IOS XR']")

#software_config_page locaters
sotware_config=(By.XPATH,'//*[@href="#device-config"]')
confi_name_id=(By.ID,'cfgName')
config_description_id=(By.ID,'cfgDescription')
next_id=(By.ID,'cfgNext')
device_n_id=(By.ID,'cfgDeviceSelect')
cmd_line_id=(By.ID,'cfgScript')
save_config=(By.ID,'cfgSave')
pop_up_xpath=(By.XPATH, '//*[@class="version-modal-box config-push-success-box"]')
pop_up_accept=(By.ID,"configPushSuccessOk")
