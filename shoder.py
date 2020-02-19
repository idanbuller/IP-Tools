import shodan

print('''


  ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄       ███▄    █        ██▓ ██▓███   ██▓ ███▄    █   █████▒▒█████  
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄     ██ ▀█   █       ▓██▒▓██░  ██▒▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒      ▒██▒▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒      ░██░▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒▒██░   ▓██░      ░██░▒██▒ ░  ░░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒       ░▓  ▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░       ▒ ░░▒ ░      ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒      ░   ░ ░        ▒ ░░░        ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
      ░   ░  ░  ░    ░ ░     ░          ░  ░         ░        ░            ░           ░            ░ ░  
                           ░                                                                             


''')

api = shodan.Shodan('')
ip = str(input("Enter IP: \n\r"))

# Lookup an IP
ipinfo = api.host(ip)

def country():
    # if ipinfo['country_name'] is None:
    #     return 'No Results'
    # elif ipinfo['country_name'] is not None:
    #     return ipinfo['country_name']
    return ipinfo['country_name'] if ipinfo['country_name'] is not None else 'No Results.'

def city():
    # try:
    #     print(ipinfo['city'])
    # except BaseException as err:
    #     return str('')
    #
    # if ipinfo['city'] is None:
    #     print("No City found")
    return ipinfo['city'] if ipinfo['city'] is not None else 'No Results.'

def ports():
    # try:
    #     print(ipinfo['ports'])
    # except BaseException as err:
    #     return str('')
    #
    # if ipinfo['ports'] is None:
    #     print("No port found")
    return ipinfo['ports'] if ipinfo['ports'] is not None else 'No Results.'

def update():
    # try:
    #     print(ipinfo['last update'])
    # except BaseException as err:
    #     return str('')
    #
    # if ipinfo['last update'] is None:
    #     print("No results found")
    return ipinfo['last_update'] if ipinfo['last_update'] is not None else 'No Results.'

def domains():
    # try:
    #     print(ipinfo['domains'])
    # except BaseException as err:
    #     return str('')
    #
    # if ipinfo['domains'] is None:
    #     print("No Domains found")
    return ipinfo['domains'] if ipinfo['domains'] is not None else 'No Results.'

def ip_string():
    # try:
    #     print(ipinfo['domains'])
    # except BaseException as err:
    #     return str('')
    #
    # if ipinfo['domains'] is None:
    #     print("No Domains found")
    return ipinfo['ip_str'] if ipinfo['ip_str'] is not None else 'No Results.'

def main():
    print(f'\nIP To Serach: \n{ip_string()} \n')
    print(f'IP Country: \n{country()} \n')
    # country()
    print(f'IP City: \n{city()} \n')
    # city()
    print(f'Open Ports: \n{ports()} \n')
    # ports()
    print(f'Last Date Updated On Shodan: \n{update()} \n')
    # update()
    print(f'Last updated: \n{domains()} \n')
    # domains()

main()


# # Search for websites that have been "hacked"
# for banner in api.search_cursor('http.title:"hacked by"'):
#     print(banner)
#
# # Get the total number of industrial control systems services on the Internet
# ics_services = api.count('tag:ics')
# print('Industrial Control Systems: {}'.format(ics_services['total']))
