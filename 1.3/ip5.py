import ipaddress

def vypocitaj_siet(ip, maska):
    ip_int = int(ipaddress.IPv4Address(ip))
    maska_int = int(ipaddress.IPv4Address(maska))
    siet_int = ip_int & maska_int
    siet = ipaddress.IPv4Address(siet_int)
    return str(siet)
    

# Dve IP adresy a ich masky
ip1 = '192.168.66.77'
maska1 = '255.255.255.0'
ip2 = '192.168.251.45'
maska2 = '255.255.255.0'

# Vypočítanie sietí
siet1 = vypocitaj_siet(ip1, maska1)
siet2 = vypocitaj_siet(ip2, maska2)

print(f"Sieť pre zariadenie s IP adresou {ip1} s maskou {maska1} je: {siet1}")
print(f"Sieť pre zariadenie s IP adresou {ip2} s maskou {maska2} je: {siet2}")

if siet1 == siet2:
    print("Zariadenia sú v rovnakej sieti.")
else:
    print("Zariadenia nie sú v rovnakej sieti.")
