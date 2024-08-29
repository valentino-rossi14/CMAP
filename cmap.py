import requests
from tabulate import tabulate
import time

ip = input("Type IP address you are looking to scan: ")
api = input("Type Criminal IP's API Key: ")

url = "https://api.criminalip.io/v1/asset/ip/report?ip={}".format(ip)
payload={}
sec_url = "https://api.criminalip.io/v1/asset/ip/report/summary?ip={}".format(ip)
sec_payload={}
headers = {
  "x-api-key": "{}".format(api)
}
start = time.time()
response = requests.request("GET", url, headers=headers, data=payload)
sec_response = requests.request("GET", sec_url, headers=headers, data=sec_payload)

if response.status_code == 200:
  try:
    output = response.json()
    sec_output = sec_response.json()
    sec_array = sec_output["current_open_ports"]["TCP"]
    third_array = sec_output["current_open_ports"]["UDP"]
    array = output["port"]["data"]
    count = output["port"]
    table = []
    printed = set()
    sec_printed = set()
    if not sec_array:
        print("No open Ports found found from IP Address {}".format(ip))
    else:
      for sec_data in sec_array:
          for data in array:
            if sec_data.get("port") == data.get("open_port_no"):
              if data.get("open_port_no") not in printed:
                port = "{}/{}".format(data.get("open_port_no"),data.get("socket"))
                status = data.get("port_status")
                service = data.get("protocol")
                version = data.get("app_version")
                list = [port,status,service,version]
                table.append(list)
                printed.add(data.get("open_port_no"))
            for third_data in third_array:
              if third_data.get("port") == data.get("open_port_no"):
                if data.get("open_port_no") not in sec_printed and data.get("socket") == "udp":
                  port = "{}/{}".format(data.get("open_port_no"),data.get("socket"))
                  status = data.get("port_status")
                  service = data.get("protocol")
                  version = data.get("app_version")
                  list = [port,status,service,version]
                  table.append(list)
                  sec_printed.add(data.get("open_port_no"))
      end = time.time()
      etime = (end -start)
      print("Scanning for open ports in IP address: {}".format(ip))
      print("\n")
      print(tabulate(table, headers=["PORT","STATE","SERVICE","VERSION"]))
      print("\n")
      print(f'Scan Finished: 1 IP address scanned in {etime:.2f} seconds')
  except KeyError:
    print("Error: Check API key Again")
else:
  print("Error", response.status_code)