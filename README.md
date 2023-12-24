# postActionScanURL
- Batch Script to be triggered as a post action by checkmarx SAST to send an email with SAST scan Results URL
    batch script expects to receive 2 arguments from SAST:
    - XML report file PATH
    - Email recipient (for now it supports only one recipient)
    
  - The batch script will call additional python script for URL extraction and sending via email
    script has variables for further customization if needed
    script output all execution info and errors to errors_log file

Python Installation: Ensure that Python is installed on the Windows server. You can direct your customer to the official Python website (https://www.python.org/) to download and install the latest version of Python. During installation, they should ensure they select the option to add Python to the system PATH to make it easier to run Python scripts from the command line.

In order to create a post scan action in sast APP  and send an email please follow these steps:
Place the 2 enclosed SCRIPT files in the Executable folder under Checkmarx home  - C:\Program Files\Checkmarx\Executables"
Open  PYTHON for edit and configure some SMTP properties – Save the file.
Create a post scan action global CONFIGURATION and in the project level as described here : https://checkmarx.com/resource/documents/en/34965-46408-configuring-an-executable-action.html#UUID-903907f7-4b20-ccb0-fc5a-fa2e6b8c5362
