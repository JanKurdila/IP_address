def ip_to_int(ip):
    # Rozdelenie IP adresy na časti
    parts = ip.split('.')
    # Prevod každej časti na celé číslo a ich vynásobenie mocninami 256
    return int(parts[0]) * 256**3 + int(parts[1]) * 256**2 + int(parts[2]) * 256**1 + int(parts[3] * 256**0)

def int_to_ip(ip_int):
    # Prevod späť na IP adresu
    octet1 = ip_int // (256**3)        # Získanie najvyššieho octetu
    octet2 = (ip_int % (256**3)) // (256**2)  # Získanie druhého octetu
    octet3 = (ip_int % (256**2)) // 256   # Získanie tretieho octetu
    octet4 = ip_int % 256            # Získanie najnižšieho octetu
    return f"{octet1}.{octet2}.{octet3}.{octet4}"

def vypocitaj_siet(ip, maska):
    ip_int = ip_to_int(ip)
    maska_int = ip_to_int(maska)
    siet_int = ip_int & maska_int
    siet = int_to_ip(siet_int)
    return siet
    

# Dve IP adresy a ich masky
ip1 = '192.168.250.46'
maska1 = '255.255.255.224'
ip2 = '192.168.250.68'
maska2 = '255.255.255.240'

# Vypočítanie sietí
siet1 = vypocitaj_siet(ip1, maska1)
siet2 = vypocitaj_siet(ip2, maska2)

print(f"Sieť pre zariadenie s IP adresou {ip1} s maskou {maska1} je: {siet1}")
print(f"Sieť pre zariadenie s IP adresou {ip2} s maskou {maska2} je: {siet2}")


if siet1 == siet2:
     print("Zariadenia sú v rovnakej sieti.")
else:
    print("Zariadenia nie sú v rovnakej sieti.")

