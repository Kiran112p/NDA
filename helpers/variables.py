
url: str = "https://networkmangement.netlify.app/"

username="Kiran112"
password="Kiran@112"

#device managemen page variables
d_name = "ROUTER_NCS_540"
d_ip ="192.168.1.100"
d_uname ="Kiran112"
d_pwd ="Kiran@112"
d_type = "IOS XR"
d_version ="7.0"
d_host ="Private"
d_protocol ="SSH"

#software_config_page variables
host_name="public_host"
value="ROUTER_NCS_540"
desription="This config changing the device host like private host to public host"
placeholder=("hostname {{public_host}}\
            ip domain-name {{domain}}")
screen_path = r"D:\NDA\reports\_after_config_job.png"

# Expected values for config job validation
expected_config_job_status = "Completed"


# software update page variables
expected_job_status="Completed"
expected_run_status="Success"
#screenshot path for software update page
screen_path="D:\\NDA\\reports\\Screenshots\\software_update_parallel.png"
#os file path for software update page
os_path=r"D:\resume\overview1.txt"

##job name for software update page
software_update_job_name="routers_Parallel_Update"