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

# Config jobs panel locators
config_panel_jobs = (By.ID, "configPanelJobs")
config_job_rows = (By.XPATH, '//*[@id="configPanelJobs"]//tbody//tr')
# first-row job name link (clickable)
config_job_name_link = (By.XPATH, '//*[@id="configPanelJobs"]//tbody//tr[1]//a')
# Modal/message shown after clicking a job
config_job_details_message = (By.ID, "configJobDetailsMessage")
# Within the job-details modal: Device and Status values
config_job_detail_device_label = (By.XPATH, '//tr[td[normalize-space()="Device"]]/td[2]')
config_job_detail_status_label = (By.XPATH, '//tr[td[normalize-space()="Status"]]/td[2]')






#software update page Locaters
su_next_btn1=(By.ID,'nextStep1')
su_next_btn2=(By.ID,'nextStep2')

file_upload=(By.XPATH,'//input[@type="file"]')
file_appeared=(By.XPATH, '//strong[contains(text(), "overview1.txt")]')

device_selection=(By.ID,"selectAllDevices")
su_job_name=(By.ID,"jobName")
instalation_type=(By.ID,"installationType")
run_now=(By.XPATH,'(//*[text()="Run now"])[1]')
srt_job=(By.ID,"startJob")

job_name = (By.XPATH, '//table[@class="jobs-table"]//tbody/tr[1]/td[2]')
job_status = (By.XPATH, '//table[@class="jobs-table"]//tbody/tr[1]/td[3]')
run_status = (By.XPATH, '//table[@class="jobs-table"]//tbody/tr[1]/td[4]')
run_time = (By.XPATH, '//table[@class="jobs-table"]//tbody/tr[1]/td[5]')
installation_type = (By.ID, "detailInstallationType")
software_image = (By.ID, "detailImage")



## validate config page locators
validate_config = (By.XPATH,'//*[@href="#validate-config"]')
device_config = (By.XPATH,'//*[@id="validateDevice"]')
expected_hostname = (By.XPATH,'//*[@id="ruleExpectedHostname"]')
run_validate_1 = (By.XPATH,'(//*[@class="fa-solid fa-play"])[2]')

device_config_os = (By.XPATH,'//*[@id="validateOsDevice"]')
device_os_version = (By.XPATH,'//*[@id="ruleExpectedOsVersion"]')
run_validate_2 = (By.XPATH,'(//*[@class="fa-solid fa-play"])[3]')