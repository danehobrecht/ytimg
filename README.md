![demonstration](https://raw.githubusercontent.com/tmuq/ytimg/main/static/media/demonstration.gif)
### Self-host
#### GNU/Linux, MacOS
1. Download the zip and create a virtual environment named "venv" in the extracted directory
```
python3 -m venv /path/to/ytimg/venv
```
2. Navigate to directory
```
cd /path/to/ytimg
```
3. Install flask
```
pip3 install flask
```
4. Establish "app.py"
```
export FLASK_APP=app.py
```
5. Run
```
python3 -m flask run
```
#### Windows
1. Download the zip and create a virtual environment (venv) in the extracted directory
```
python3 -m venv c:path\to\ytimg\venv
```
2. Activate virtual environment
```
venv\Scripts\activate.bat
```
3. Install dependencies
```
pip3 install flask
```
4. Establish "app.py"
```
set FLASK_APP=app.py
```
5. Run
```
python3 -m flask run
```
### Prerequisites
 - Python 3.9.2 & pip3
https://www.python.org/downloads/
 - virtualenv
https://pypi.org/project/virtualenv/
