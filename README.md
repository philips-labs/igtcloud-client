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
  download   Download data from Philips Interventional Cloud
  get-token  Get token for Philips Interventional Cloud     
  login      Login to Philips Interventional Cloud
  upload     Upload data to Philips Interventional Cloud    
  version    Print version of this tool
```

Use ```igtcloud [command] --help``` for more information about a command

## Upload folder structure
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
│   │   series_1.dcm
│   │   series_2.dcm
    │   ...
│   │
│   └─── subfolder1
│       │   series_3.dcm
│       │   series_4.dcm
│       │   ...
│
└─── institute2
    │   series_1.dcm
    │   series_2.dcm
    │   ...
    │
    └─── subfolder1
    │   │   series_3.dcm
    │   │   series_4.dcm
    │   │   ...
    │
    └─── subfolder2
        │   series_5.dcm
        │   series_6.dcm
        │   ...
```

Where `local_folder` is the specified LOCAL_FOLDER via the `upload` command.

### Uploading project-level files

Files under the `local_folder/files` directory will be uploaded directly to the specified PROJECT via the `upload` command.

### Uploading institute-level files

Folders under the institute-named folders (`local_folder/<institute name>`) will be uploaded directly to the institute as a study then the nested folders are uploaded as normal study-level folders.

Other folders/files under the `local_folder` directory will be ignored.

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