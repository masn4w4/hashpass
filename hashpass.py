#!/usr/bin/env python
from urllib import urlopen, urlencode
from re import search
import sys, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Masukan hash.txt kamu disini", dest='path')
args = parser.parse_args()

#Colors and shit like that
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[>]\033[1;m'

def omega():
    data = urlencode({"hash":hashvalue, "decrypt":"Decrypt"})
    html = urlopen("http://md5decrypt.net/en/Sha256/", data)
    find = html.read()
    match = search (r'<b>[^<]*</b><br/><br/>', find)
    if match:
        print "\n%s %s : " % (good, hashvalue), match.group().split('<b>')[1][:-14]
    else:
        if not args.path:
            print "%s Maaf ya Hash kamu gak ada di database kami." % bad

def Lambda():
    html = urlopen("http://md5decrypt.net/Api/api.php?hash=%s&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728" % hashvalue)
    find = html.read()
    if len(find) > 0:
        print "\n%s %s : " % (good, hashvalue), find
    else:
        if not args.path:
            print "%s Maaf ya Hash kamu gak ada di database kami." % bad
def beta():
    data = urlencode({"auth":"8272hgt", "hash":hashvalue, "string":"","Submit":"Submit"})
    html = urlopen("http://hashcrack.com/index.php" , data)
    find = html.read()
    match = search (r'<span class=hervorheb2>[^<]*</span></div></TD>', find)
    if match:
        print "\n%s %s : " % (good, hashvalue), match.group().split('hervorheb2>')[1][:-18]
    else:
        omega()
print ((56 * '\033[1;31m-'))
print "\t%s     By n4w4_cc" % (white, red, end, white)
print """
            _____           _____   __                .__          
  ____    /  |  |__  _  __/  |  |_/  |_  ____   ____ |  |   ______
 /    \  /   |  |\ \/ \/ /   |  |\   __\/  _ \ /  _ \|  |  /  ___/
|   |  \/    ^   /\     /    ^   /|  | (  <_> |  <_> )  |__\___ \ 
|___|  /\____   |  \/\_/\____   | |__|  \____/ \____/|____/____  >
     \/      |__|            |__|                              \/ 
                                                                                                                                     
                                                           
                                    
"""
print ((56 * '\033[1;31m-'))

def crack(hashvalue):
    if len(hashvalue) == 32:
        if not args.path:
            print "%s Tipe Hash : MD5" % info
        data = urlencode({"hash":hashvalue,"submit":"Decrypt It!"})
        html = urlopen("http://md5decryption.com", data)
        find = html.read()
        match = search(r"Decrypted Text: </b>[^<]*</font>", find)
        if match:
            print "\n%s %s : " % (good, hashvalue), match.group().split('b>')[1][:-7]
        else:
            data = urlencode({"md5":hashvalue,"x":"21","y":"8"})
            html = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data)
            find = html.read()
            match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", find)    
            if match:
                print "\n%s %s :" % (good, hashvalue), match.group().split('span')[2][3:-6]
            else:
                url = "http://www.nitrxgen.net/md5db/" + hashvalue
                purl = urlopen(url).read()
                if len(purl) > 0:
                    print "\n%s %s :" % (good, hashvalue), purl
                else:
                    if not args.path:
                        print "%s Maaf ya Hash kamu gak ada di database kami." % bad
    elif len(hashvalue) == 40:
        if not args.path:
            print "%s Tipe Hash : SHA1" % info
        beta()
    elif len(hashvalue) == 64:
        if not args.path:
            print "%s Tipe Hash : SHA-256" % info
        Lambda()
    else:
        print "%s Yaaah hash kamu tidak mendukung sistem." % bad

if args.path:
    hashes = []
    with open(args.path, 'r') as f:
        for line in f:
            hashes.append(line.strip('\n'))
    for hashvalue in hashes:
        crack(hashvalue)
else:
    hashvalue = raw_input('%s Masukkan hash kamu disini: ' % que).lower()
    crack(hashvalue)
