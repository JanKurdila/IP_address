def ip_to_bin(ip):
    # Rozdelenie IP adresy na časti
    parts = ip.split('.')
    bin_ip = ''
    
    # Prevod každej časti na binárny reťazec s dĺžkou 8 bitov a spájanie všetkých častí do jedného reťazca
    for part in parts:
        bin_part = bin(int(part))[2:]  # Prevod na binárny reťazec a odstránenie prefixu '0b'
        
        # Doplníme binárny reťazec na 8 bitov pomocou for cyklu
        dopln_nuly_na_zaciatok = 8 - len(bin_part)
        for _ in range(dopln_nuly_na_zaciatok):
            bin_part = '0' + bin_part
        
        bin_ip += bin_part
    
    return bin_ip

def bin_to_ip(bin_ip):
    # Rozdelenie binárneho reťazca na časti po 8 bitov
    parts = []
    for i in range(0, 32, 8): # for i in range(4):
        parts.append(bin_ip[i:i+8])
    
    # Prevod každej časti na dekadické číslo a spájanie všetkých častí do IP adresy
    ip = ''
    for part in parts:
        ip += str(int(part, 2)) + '.'
    
    # Odstránenie poslednej bodky
    ip = ip.rstrip('.')
    
    return ip

def vypocitaj_siet(ip, maska):
    bin_ip = ip_to_bin(ip)
    bin_maska = ip_to_bin(maska)
    
    # Logická operácia AND na jednotlivých bitoch IP adresy a masky
    bin_siet = ''
    for i in range(32):
        if bin_ip[i] == '1' and bin_maska[i] == '1':
            bin_siet += '1'
        else:
            bin_siet += '0'
    
    # Prevod binárnej adresy siete na dekadický formát
    siet = bin_to_ip(bin_siet)
    
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
