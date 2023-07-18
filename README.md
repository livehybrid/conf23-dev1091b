# Introduction
This is intended to assist users in the DEV1091B workshop at Splunk .conf23 in Las Vegas, however you may find some of these resources helpful when starting out using Splunk's UCC app framework.  

The aim of the workshop is to introduce you to UCC and walk through how to get started with a simple API data collection example. In this case we are pulling energy usage data from [Equine Energy's API](https://energyapi.splunk.engineer)).  

*Note: Equine Energy is a ficitious company used for the purposes of the workshop. We intend to keep the API available for a number of weeks after the conference to allow you to continue using it for development.*

# Prerequisites
* UCC
  * `pip install splunk-add-on-ucc-framework`
* SLIM ([Splunk Packaging Toolkit](https://dev.splunk.com/enterprise/docs/releaseapps/packageapps/packagingtoolkit/))
  * `pip install splunk-packaging-toolkit`  
   or  
   [Download package Tarball](https://download.splunk.com/misc/packaging-toolkit/splunk-packaging-toolkit-1.0.1.tar.gz) and install with `pip install splunk-packaging-toolkit-1.0.1.tar.gz` 
* API Key
  *  Follow instructions at https://energyapi.splunk.engineer/

# Snippets
* Validate UCC is installed and working:  
 `ucc-gen --help`

* Create Barebones app  
`ucc-gen init --addon-name "ta_equine_energy" --addon-display-name "Equine Energy Add-on for Splunk" --addon-input-name energy_usage  
`
* Build app:
` ucc-gen build --ta-version 1.0.0`  
* Package app:
`slim package output/ta_equine_energy`  

## Code addition
```
def get_data_from_api(logger: logging.Logger, api_key: str):
    logger.info("Getting data from an external API")
    resp = requests.get(
                "https://energyapi.splunk.engineer/getUsage",
                headers = {"x-api-key":api_key}
            )
    return resp.json()
```
Also see the full Python script [energy_usage.py](./app/energy_usage.py)

# Useful Links
*  [Splunk Python SDK](https://docs.splunk.com/DocumentationStatic/PythonSDK/1.2.2/modularinput.html)
* [Splunk Community Slack - #ucc-framework](https://splunk-usergroups.slack.com/archives/C03SG3ZL4S1)
* [Splunk Answers](https://community.splunk.com/)
* Other Splunk apps using UCC - https://github.com/splunk/ 
