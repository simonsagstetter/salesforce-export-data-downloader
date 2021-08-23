## Salesfroce Export Data Downloader
In Salesforce Enterprise, Performance, Unlimited, and Developer editions you can schedule a weekly export of your whole salesforce organization data. When the export is finished you can download a zip archive containing all your data from your salesforce setup. With the Salesforce Export Data Downloader you can extend this feature and let a python script download your exported data automatically. All you need to do is to configurate your credentials and organization information and bind the run.py as a task to your windows task scheduler or linux cron job tab.

### Installation

> Download the repository and install the dependencies
```
  pip install -r requirements.txt
```

### Configuration

> Open the config.json and enter your credentials and salesforce organization information. The user needs to have access to the export data home.
```json
  {
    "username": "<your_username",
    "password": "<your_password>",
    "security_token": "<your_orgs_security_token>",
    "auth_url": "<your_domain>.my.salesforce.com/services/Soap/u/<Version>",
    "org_url": "<your_domain>.my.salesforce.com",
    "sender": "",
    "receiver": ""
  }
```

### Download

> If your configuration is done you can already test the downloader by executing the run.py script. 
> MAKE SURE THAT THERE IS AN EXPORT AVAILABLE IN YOUR EXPORT DATA HOME!

```
  python run.py
```

![image](https://user-images.githubusercontent.com/44363600/129879594-03bf43c4-d940-483a-bc53-c0bbd14ed07a.png)
