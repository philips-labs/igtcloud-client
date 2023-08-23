# IGT Cloud Client

Python client for the Philips IGT Cloud Datalake.

Includes both a Python interface and a CLI (Command line interface) to perform the most common tasks.
## Overview

1. [CONTRIBUTING.md](./CONTRIBUTING.md)
2. [CHANGELOG.md](./CHANGELOG.md)
3. [CODE_OF_CONDUCT](./CODE_OF_CONDUCT.md)
4. [MAINTAINERS](./MAINTAINERS.md)
5. [LICENSE](./LICENSE)

## Getting Started

- Setup a Python 3 environment
- pip install git+https://github.com/philips-labs/igtcloud-client
- -OR- use the [standalone CLI](https://github.com/philips-labs/igtcloud-client/releases/latest) that doesn't require a Python installation

## CLI
```
Usage: igtcloud [OPTIONS] COMMAND [ARGS]...                         
                                                                    
  Philips Interventional Cloud CLI                                  
                                                                    
Options:                                                            
  --help  Show this message and exit.                               
                                                                    
Commands:                                                           
  csv        List data from Philips Interventional Cloud in CSV file
  download   Download data from Philips Interventional Cloud        
  get-token  Get token for Philips Interventional Cloud             
  login      Login to Philips Interventional Cloud                  
  upgrade    Upgrade this tool to a new version                     
  upload     Upload data to Philips Interventional Cloud            
  version    Print version of this tool
```

Use ```igtcloud [command] --help``` for more information about a command

### Login

The `igtcloud login` command is a special CLI command that will do the authentication with Philips Interventional Cloud.
This decouples the login flow from the real applications, which is particularly useful during development and testing.
It prevents that you have to type your password everytime.

This command will automatically refresh your token until you interrupt the process (`Ctrl + c`).

The `download`, `upload` and `csv` commands are compatible with the `login` command.
The `get-token` is available if you require an access token outside the IGT Cloud Client (CLI or Python).

#### Service login

A special option for the `login` command is to use a service identity.
This requires that you have a `service_id` and matching `private_key`

To use this service login you have to provide the private_key using the CLI:

`igtcloud login -d <DOMAIN> -u <SERVICE_ID> -s <PRIVATE_KEY_FILENAME>`

For convenience, you can discard the `-u <SERVICE_ID>`. Now the service_id will be the same as the private key filename without extension (e.g. `igtcloud login -d <DOMAIN> -s service_x@institute.project.philips.com.pem` will use `service_x@institute.project.philips.com` as `SERVICE_ID` and the content of the file as `PRIVATE_KEY`)

To create a service identity you can use the following python example code:

(this requires one of the following roles: `DATA_MANAGER` on the project or `COORDINATOR` or `INVESTIGATOR` on the institute. Next it requires a user specific role `SERVICES_MANAGER`)
```python
from igtcloud.client.core.auth import smart_auth
from igtcloud.client.services import entities_service, set_auth
from igtcloud.client.services.entities.model.service import Service
from igtcloud.client.services.utils.key import save_private_key

domain = '<DOMAIN>'
institute_id = '<INSTITUTE_ID>'
service_name = '<SERVICE_NAME>'

with smart_auth(domain) as auth:
    set_auth(auth)

    service = entities_service.post_services(institute_id, Service(name=service_name))
    save_private_key(service.private_key, f"{service.service_id}.pem")
```

> **_Note:_** Service identities can only be used for uploading data, not downloading.

## Folder structure

### Flat (default)

```
local_folder
│
└─── files
│   │   file_1.txt
│   │   file_2.txt
│   │   ...
│   │
│   └─── subfolder1
│       │   file_3.txt
│       │   file_4.txt
|       │   ...
│
└─── institute1
    │
    └─── patient1---study1
    │   │   series_1.dcm
    │   │   series_2.dcm
    │   │   ...
    │
    └─── patient1---study2
    │   │   series_1.dcm
    │   │   series_2.dcm
    │   │   ...    
    │
    └─── patient2---study1
        │   series_1.dcm
        │   series_2.dcm
        │   ...
```

### Hierarchical

```
local_folder
│
└─── files
│   │   file_1.txt
│   │   file_2.txt
│   │   ...
│   │
│   └─── subfolder1
│       │   file_3.txt
│       │   file_4.txt
|       │   ...
│
└─── institute1
    │
    └─── patient1
    │   │
    │   └─── study1
    │   │   │   series_1.dcm
    │   │   │   series_2.dcm    
    │   │   │   ...
    │   │
    │   └─── study2
    │       │   series_1.dcm
    │       │   series_2.dcm    
    │       │   ...    
    │
    └─── patient2
    │   │
    │   └─── study1
    │       │   series_1.dcm
    │       │   series_2.dcm    
    │       │   ...
```

Where `local_folder` is the specified LOCAL_FOLDER via the `upload` or `download` command.

### Project-level files

Files under the `local_folder/files` directory will be uploaded/downloaded based on the passed PROJECT argument via the `upload` or `download` command.

> **_Note:_** for the `download` command, this will only work if the `--project-files` option is passed. 

### Upload institute-level files

Folders under the institute-named folders (`local_folder/<institute name>`) will be uploaded directly to the institute as a study then the nested folders are uploaded as normal study-level folders.

Other folders/files under the `local_folder` directory will be ignored.

### Download institute-level files

Institutes will be downloaded to the LOCAL_FOLDER argument and will create sub folders based on the institute name. 

#### Flat

In `flat` file structure mode (default), all studies of each institute will be downloaded as flat subdirectories under each institute folder.
The folder name will be a combination of the patient and study identifiers.

#### Hierarchical 

In `hierarchical` file structure mode, all studies of each institute will be downloaded in a nested folder structure.
In the institute folder, the first level of directories will resemble the patients. 
Each patient folder will contain nested folder for each study that belongs to this patient.

## Developers

### Generate code based on new OpenAPI specification

```BASH
./code-gen.sh
```

### Test the cli locally

```BASH
cd src
python cli.py
```

### Community

This project uses the [CODE_OF_CONDUCT](./CODE_OF_CONDUCT.md) to define expected conduct in our community. Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting a project [MAINTAINER](./MAINTAINERS.md)

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more info on what's been changed.

## Licenses

See [LICENSE](./LICENSE)
