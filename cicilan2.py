import datetime

currentyear = datetime.date.today().year

def coba(pilih):
    
    if (pilih =="Manual"):
        kendaraan = input("Pilih Motor | Mobil :\n")
        if (kendaraan.lower() != "motor"):
            if (kendaraan.lower() != "mobil"):
                return "salah"
        if (kendaraan.lower() != "mobil"):
            if (kendaraan.lower() != "motor"):
                return "salah"
        kondisi = input("Pilih Baru | Bekas :\n")
        if (kondisi.lower() != "baru"):
            if (kondisi.lower() != "bekas"):
                return "salah"
        if (kondisi.lower() != "baru"):
            if (kondisi.lower() != "bekas"):
                return "salah"
        tahun = int(input ("Input Tahun Kendaraan :\n"))
        if (kondisi =="baru"):
            if (tahun<(currentyear-1)):            
                return "salah"
        pinjamantotal = float(input("Input Jumlah Pinjaman Total :\n"))
        tenor = int(input("Input Tenor Pinjaman 1-6 Tahun :\n"))
        if (tenor > 6):
            return ("salah")
        dp = float(input("Input Jumlah DP :\n"))
        if ((kendaraan.lower() == "motor" or kendaraan.lower()=="mobil") and kondisi.lower()=="bekas"):        
            if(dp<=(0.35*pinjamantotal)):            
                return "salah"
        if ((kendaraan.lower() == "motor" or kendaraan.lower()=="mobil") and kondisi.lower()=="baru"):        
            if(dp<=(0.25*pinjamantotal)):            
                return "salah"
        if (kendaraan.lower() == "motor"):
            interest = 0.08
        if (kendaraan.lower() == "mobil"):
            interest = 0.09
        print ("\n")
        print ("\n")
        print ("\n")
        print ("--------Output--------")
        print ("Kendaraan : "+kendaraan)
        print ("Status : "+kondisi)
        print ("Tahun : "+str(tahun))
        print ("Jumlah Pinjaman : "+ str(pinjamantotal))
        print ("Jumlah Tenor : "+ str(tenor))
        print ("Jumlah DP : "+ str(dp))
        print ("Simulasi Credit :")
        rumus = (pinjamantotal/4)/12
        for x in range(tenor):
            if ((x+1)>1):
                if (x%2==0):
                    interest = interest+0.5                
                else:
                    interest = interest +0.1
                rumus = rumus + (rumus * interest)
            else:
                rumus = rumus + (rumus * interest)
            print("Tahun "+str(x+1)+": Rp"+str(rumus)+" /bln, Suku Bunga : "+str(interest))
    elif (pilih.lower() == "file"):
        filename = input("Masukkan nama file: \n")+".txt"
        with open(filename) as filehandle:
            data = filehandle.read()
            parsingenter = data.split('\n')
        total = len(parsingenter)
        for i in range(total):
            parsingspasi = parsingenter[i].split()
            
            if (i==0):
                kendaraan = parsingspasi[1]
                if (kendaraan.lower() != "motor"):
                    
                    if (kendaraan.lower() != "mobil"):
                        return "salah"
                if (kendaraan.lower() != "mobil"):
                    if (kendaraan.lower() != "motor"):
                        return "salah"
            elif (i==1):
                kondisi = parsingspasi[1]
                if (kondisi.lower() != "baru"):
                    if (kondisi.lower() != "bekas"):
                        return "salah"
                if (kondisi.lower() != "baru"):
                    if (kondisi.lower() != "bekas"):
                        return "salah"
            elif (i==2):
                tahun = int(parsingspasi[1])
                if (kondisi =="baru"):
                    if (tahun<(currentyear-1)):            
                        return "salah"                
            elif (i==3):
                pinjamantotal = float(parsingspasi[1])              
            elif (i==4):
                tenor = int(parsingspasi[1])
                if (tenor > 6):
                    return ("salah")
            elif (i==5):
                dp = float(parsingspasi[1])
            else:
                return "salah"
        if ((kendaraan.lower() == "motor" or kendaraan.lower()=="mobil") and kondisi.lower()=="bekas"):        
            if(dp<=(0.35*pinjamantotal)):            
                return "salah"
        if ((kendaraan.lower() == "motor" or kendaraan.lower()=="mobil") and kondisi.lower()=="baru"):        
            if(dp<=(0.25*pinjamantotal)):            
                return "salah"
        if (kendaraan.lower() == "motor"):
            interest = 0.08
        if (kendaraan.lower() == "mobil"):
            interest = 0.09
        print ("\n")
        print ("\n")
        print ("\n")
        print ("--------Output--------")
        print ("Kendaraan : "+kendaraan)
        print ("Status : "+kondisi)
        print ("Tahun : "+str(tahun))
        print ("Jumlah Pinjaman : "+ str(pinjamantotal))
        print ("Jumlah Tenor : "+ str(tenor))
        print ("Jumlah DP : "+ str(dp))
        print ("Simulasi Credit :")
        rumus = (pinjamantotal/4)/12
        for x in range(tenor):
            if ((x+1)>1):
                if (x%2==0):
                    interest = interest+0.5                
                else:
                    interest = interest +0.1
                rumus = rumus + (rumus * interest)
            else:
                rumus = rumus + (rumus * interest)
            print("Tahun "+str(x+1)+": Rp"+str(rumus)+" /bln, Suku Bunga : "+str(interest))
    else:
        return "salah"
loop = True
while loop:
    pilih = input("Pilih input Manual | File\n")
    a = coba(pilih)
    if (a=="salah"):
        print ("salah input")
    
             
