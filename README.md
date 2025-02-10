# pdf2word

~~60 lines~~40 lines of code implement multi-process PDF to Word conversion

> New version implemented based on [https://github.com/dothinking/pdf2docx](https://github.com/dothinking/pdf2docx)

## Usage

* Clone or download the project locally
```python
git clone git@github.com:simpleapples/pdf2word.git
```

* Enter the project directory, create a virtual environment, and install dependencies

```python
cd pdf2word
python3 -m venv venv

# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# Python < 3.10
pip install -r requirements.txt

# Python 3.10 or later
pip install -r requirements_3_10.txt
```

* Modify the config.cfg file to specify the folders for storing PDF and Word files, as well as the number of concurrent processes
* Run ```python main.py```

## ModuleNotFoundError: No module named '_tkinter' error handling

### macOS environment

1. Install homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Use homebrew to install tkinter
```bash
brew install python-tk
```

### Linux environment

Take Ubuntu as an example

```bash
sudo apt install python3-tk
```

**Welcome to Star**

## Python Cookbook

![](http://ww1.sinaimg.cn/large/6ae0adaely1foxc0cfkjsj2076076aac.jpg)

## License

Licensed under the MIT License
