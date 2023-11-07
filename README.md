# client-tcp-msg

Sending messages of one or more lines, this message is retrieved from a text file

# How to use?

### 1.- Config

Edit config.json

```
{
    "host": "127.0.0.1",
    "port": 12345,
    "bit": 262144
}
```

**host**: server to which the message is directed.

**port**: port of communication to the server.

**bit**: limit of information to send.

### 2.- Send message

**Python**

```
python client.py target_file.txt
```

**Windows dist**
```
client.exe target_file.txt
```

# Dev

### Install venv

Create a new virtual environment.

```
python -m venv venv
```

Activate the virtual environment.

- Windows option:
  
    ```
    venv/Scripts/Activate.ps1
    ```

- Other

    ```
    source venv/bin/activate
    ```
    
Install requirements

```
pip install -r ./requirements.txt
```

