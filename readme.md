# CMAP
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## What is CMAP?
**CMAP** is a python script that scans for open ports at certain IP address and gives NMAP-like table results of the information about open ports. 

## Prerequisites
1. *API key from Criminal IP* is needed to run the script (You can get it from [criminalip.io](criminalip.io))
2. This script uses *requests and tabulate module*
3. Made in *Python 3*

## How to Run
run `cmap.py` 
You will be asked to type in two things.
1. IP address (It will not accept *IPv6* address)
2. API key from Criminal IP

After these two inputs, the script will scan and filter results to give you the report of the current open ports. 

## Screen
![result](https://github.com/user-attachments/assets/0a5c1ad8-0cf6-43e0-a60d-023e84882033)

## Results
The results will be in table format showing the *port number*, *state*, *socket* and *version*.
It will also show the *time* it took to run the script.


> [!CAUTION]
> **If the Error code returns 400, it usually means that you have typed in IPv6 address**. <br> If you typed just enter key on either IP address or API key input it will give you error saying <br> *"Error: Check API key Again"*
