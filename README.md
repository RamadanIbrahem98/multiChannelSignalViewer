# multiChannelSignalViewer

<p align="center">
  <img src="https://img.shields.io/github/license/RamadanIbrahem98/multiChannelSignalViewer?style=plastic&logo=appveyor&color=blue" alt="license" />
  <img src="https://img.shields.io/github/last-commit/RamadanIbrahem98/multiChannelSignalViewer?style=plastic&logo=appveyor" alt="last-commit" />
</p>

<p align="center">
    <img src="UI/assets/Preview.gif" />
</p>

## Table of Contents

-   [About the Project](#about-the-project)
-   [Toolbox](#toolbox)
-   [Setting Up the Environment](#setting-up-the-environment)

## About The Project

This is a Multi-Channel Bio-Signal Viewer GUI Application

## Toolbox

-   Python
    -   PyQt5
    -   pyqtgraph
    -   FPDF
    -   Scipy

## Setting Up the Environment

1. Clone the repo
    - HTTPS
        ```sh
        git clone https://github.com/RamadanIbrahem98/multiChannelSignalViewer.git
        ```
    - SSH
        ```sh
        git clone git@github.com:RamadanIbrahem98/multiChannelSignalViewer.git
        ```
1. Create a Virtual Environment (Optional)
    ```sh
    python -m venv .env
    ```
1. Activate the virtual environment

    - using CMD
        ```sh
        .\.env\Scripts\activate
        ```
    - using PowerShell
        ```sh
        .\.env\Scripts\Activate.ps1
        ```
    - using Bash
        ```sh
        source .env/bin/activate
        ```

1. Install the requirements and dependancies
    ```sh
    pip install -r requirements.txt
    ```
1. Run the application
    ```sh
    python main.py
    ```
