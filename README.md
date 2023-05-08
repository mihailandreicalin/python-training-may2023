# Python Training

## Project installation with PyCharm

1. Clone the repository inside `PycharmProjects` directory:

    ```shell
    cd ~/PycharmProjects/
    git clone https://github.com/iuliachiriac/python-training-may2023.git
    ```

1. Open PyCharm, go to `File` -> `Open` and select the `python-training-may2023` directory.
1. In PyCharm, go to `Preferences/Settings` -> `Project:python-training-may2023` -> `Project Interpreter`
1. Click on the settings icon -> `Add` -> `+` icon.
1. Select `Virtualenv Environment` -> check `New environment` and make sure Python3 installation path is correctly selected under `Base interpreter` -> `Ok`.
1. After the virtual environment is created, go to `Terminal` tab. The virtual environment should be activated (you should see `(venv)` before the usual prompt).

1. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

## Project installation without PyCharm

1. Clone the repository:

    ```shell
    git clone https://github.com/iuliachiriac/python-training-may2023.git
    ```

1. Move to project directory:
    ```shell
    cd python-training-may2023
    ```

1. Create a virtual environment:

    ```shell
    virtualenv venv
    ```

1. Activate virtual environment:

    Linux/MacOS:
    ```shell
    source venv/bin/activate
    ```

    Windows:
    ```shell
    venv\Scripts\activate
    ```

1. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

### Contact
Iulia Chiriac <iulia.chiriac.a@gmail.com>
