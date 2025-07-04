# Module hpe-sample 

Provide a description of the purpose of the module and any relevant information.

## Model hpe-automotive:hpe-sample:sample-sensor

Provide a description of the model and any relevant information.

### Configuration
The following attribute template can be used to configure this model:

```json
{
"attribute_1": <float>,
"attribute_2": <string>
}
```

#### Attributes

The following attributes are available for this model:

| Name          | Type   | Inclusion | Description                |
|---------------|--------|-----------|----------------------------|
| `attribute_1` | float  | Required  | Description of attribute 1 |
| `attribute_2` | string | Optional  | Description of attribute 2 |

#### Example Configuration

```json
{
  "attribute_1": 1.0,
  "attribute_2": "foo"
}
```

### DoCommand

If your model implements DoCommand, provide an example payload of each command that is supported and the arguments that can be used. If your model does not implement DoCommand, remove this section.

#### Example DoCommand

```json
{
  "command_name": {
    "arg1": "foo",
    "arg2": 1
  }
}
```


## Viam Module Development Setup on Windows

You can follow this [tutorial](https://code.visualstudio.com/docs/remote/wsl) for the steps 1-3.

1. Install WSL "Windows Subsystem for Linux"
2. Install Visual Studio Code (my recommendation)
3. Install Visual Studio Code WSL Extension
4. [Clone](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_clone-a-repository-locally) this repo from within Visual Studio Code
5. [Open a terminal](https://code.visualstudio.com/docs/terminal/basics) within Visual Studio Code and run the setup script `./setup.sh`

## Install Viam Server in WSL

1. [Open a terminal](https://code.visualstudio.com/docs/terminal/basics) within Visual Studio Code connected to WSL
2. Create a machine in app.viam.com and use the linux commands to install Viam Server into your WSL instance