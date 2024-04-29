# Enscape Patcher

## 💭 About
Enscape addon proxy patch. More informations about [Enscape here](https://enscape3d.com).

Tested up to Enscape 4.0 on macOS 14.x

![Licence](https://i.imgur.com/EZ7l0Dk.png)

## 🚀 Installation

1. Create a specific virtual environment with venv using `python3 -m venv env`
2. Then source it with `source ./env/bin/activate`
3. Install requirements with `pip install -r requirements.txt`

## 📦 Create Bundle

1. Read the content of `package.sh`
2. Set the rights with `chmod +x package.sh`
3. Create the bundle with `./package.sh`
4. `Enscape Patcher` will be into the `dist` folder

## 🔥 Usage

Execute the executable `Enscape Patcher` or with Python 3:

```
python app.py
```

Then set the proxy into the Enscape network settings:
- `address`: `127.0.0.1`
- `port`: `6666`

![Enscape Patcher](https://i.imgur.com/ttzr08h.png)
![Enscape proxy](https://i.imgur.com/285DWQS.png)


## 🛠️ Dependencies

- [mitmproxy](https://pypi.org/project/mitmproxy/)

## 🤝 Contributing

If you are interested in helping contribute to this repository, do not hesitate to create a pull request!

## 🔮 TODO

- Make a Sketchup addon with Enscape Patcher bundled

## 📝 License

Copyright © 2024-present, [Contributors](https://github.com/AkdM/EnscapePatcher/graphs/contributors).<br>
This project is [GNU LGPLv3](https://github.com/AkdM/EnscapePatcher/blob/master/LICENSE) licensed.