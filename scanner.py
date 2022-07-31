import requests, argparse, sys
from colorama import *

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url", required=True)
parser.add_argument("-p", "--payloads", help="payloads list", required=True)
args = parser.parse_args()

def fuzz(url, payloads):
    payloads = open(payloads, "r").readlines()
    for payload in payloads:
        new_url = url.replace('{fuzz}', payload)
        request = requests.get(new_url)
        if request.elapsed.total_seconds > 7:
            print(Style.BRIGHT + Fore.RED + "Timeout detected with", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not working with this payload :", payload)

def verif(url):
    url_test = url.replace('{fuzz}', "")
    req = requests.get(url_test)
    if req.elapsed.total_seconds() > 6:
        sys.exit(Style.BRIGHT + Fore.RED + "Please make sure you have a good connection to run the scanner")
    else:
        fuzz(args.url, args.payloads)

if not '{fuzz}' in args.payload:
    sys.exit(Style.BRIGHT + Fore.RED + "Missing {fuzz} parameter!")
else:
    verif(args.url)


#how to use
#python scanner.py -u "<url>{fuzz}" -p payloads.txt
#replace <url> with the website you want to scan, do not remove "{fuzz}"
#create a payload file named payloads.txt

