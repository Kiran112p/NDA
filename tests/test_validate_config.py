from pages import device_management_ssh_private
from pages import validate_config_module

class TestValidateConfig:
    def test_validate_config(self, driver):
        
        device_management = device_management_ssh_private.DeviceManagementPage(driver)

        #navigate to device management page and add a device
        device_management.navigate_to_device_management()
       
        #device adding 
        device_management.add_device()
        

        # Create an instance of the ValidateConfigModule class
        validate_config = validate_config_module.ValidateConfigModule(driver)

        # Navigate to the validate config page
        validate_config.navigate_to_validate_config()

        # Select the device for validation
        validate_config.validate_hostname()

        # Enter the expected hostname
        validate_config.host_name()

        # Run the validation
        validate_config.run_validate()

        # Validate the config job status
        validate_config.validate_config_job_status()

        #validae the os version
        validate_config.os_version()

        # Enter the expected os version
        validate_config.expected_os_version()

        # Run the os validation
        validate_config.run_os_validate()
        
        # Validate the os job status
        validate_config.validate_os_job_status()
