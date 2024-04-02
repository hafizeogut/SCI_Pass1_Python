import math

def hexadecimal_to_decimal(x):
    decimal_number = 0 #Onluk tabana çevrilen sonucu tutacak değişken
    count = 0 #sayac
    
    while x != 0: #Girdi sıfır olana kadar devam et 
        remainder = x % 10 #Girdinin 10'a bölümünden kalan alındı 
        decimal_number += remainder * 16 ** count #Kalan, onaltılık tabandaki sayıya çevrildi ve sonuca eklendi
        x = x // 10 #Girdi ondalık tabana çevrildi
        count += 1 #Saayaç arttırıldı
    
    return decimal_number #Onluk tabana çevrilen sayı döndürüldü.

def read_line_from_file(src, pos):
    line = "" #Satırı saklayacak değişken oluşturuldu.
    src.seek(pos) #Dosya belirli konuma girildi.
    line = src.readline()#Dosyadan bir satır okundu.
    pos = src.tell()#Dosyanın son konumu saklandı.
    return line, pos #Okunan satır ve son konum döndürüldü.

def break_line(line):
    fields = line.split("\t") #Satır, sekme kararkterine parçalandı
    label = opcode = operand = rest = ""#Etiket,opcode,operand ve  geri kalan kısımlar için boşi dizeler oluşturuldu.
    
    if len(fields) >= 1:#Eğer satırın en az bir öğesi varsa:
        label = fields[0].strip()#İlk öğe, etiket olarak belirlendi ve sonunsdaki boşluklar temizlendi.
        
    if len(fields) >= 2:# Eğer satırın en az iki öğesi varsa:
        opcode = fields[1].strip()#İkinci öğe,opcode olarak kabul edilir ve diğer boşluklar temizlenir.
        
        
    if len(fields) >= 3:#Eğe satırın en az üç öğesi varsa:
        operand = fields[2].strip()#Üçüncü öğe,operand olarak kabul edilir ve baş ve sondaki boşluklar temizlenir. 
        
    if len(fields) >= 4:#Eğer satırın en az dört öğesi varsa
        rest = fields[3].strip()#Dördüncüğ öğe ve sonrası silinir.
        
    return label, opcode, operand, rest # Parçalanan etiket, opcode, operand ve geri kalan kısımlar döndürülür

def search_symtab(label):
    found = False#Etikeitn bulunup bulunmadığını belirten bayrak oluşturuldu.
    
    #symtab.txt dosyası okuma modunda açıldı 
    with open("symtab.txt", "r") as symtab:
        
        #Dosyanın her satırı için döngü oluşturuldu.
        for line in symtab:          
            symbol, value = line.split()#Satırdaki sembol ve değer, boşluk karakterine göre ayrıldı.
            if symbol == label:#Eğer satırdaki sembol,aranan etiketle eşleşiyorsa
                found = True #Bulundu bayrağı olarak  işaretlendi.
                break
    return found #bulundu bayrağı döndüğrüldü.

def search_optab(opcode):# verilen bir opcode'un optab.txt dosyasında bulunup bulunmadığını kontrol etmektir.
    found = False #Opcode var mı bayrağı oluşturuldu.
    
    with open("optab.txt", "r") as symtab:# "optab.txt" dosyası okuma modunda açıldı ve "symtab" adı altında kullanıldı
        for line in symtab:#Dosyanın her satırı için döngü oluşturuldu.
            symbol, value = line.split()#Satırdaki sembol ve değer,boşluk karakterine göre ayrıldı.
            if symbol == opcode:#Eğer satırdaki sembol,aranan opcode ile eşleşiyorsa
                found = True#bulundu
                break
    return found #Bulundu bayrağı döndürüldü.

                        
def main():
    startaddress = locctr = proglength = 0
    #Başlangıç adresi,konumu,program uzunluğu 0 ile başltıldı.
    progname = "" #Program ismi için boş satır oluşturuldu.


    #Kaynak dosyası ("src.txt") okuma modunda açıldı.
    with open("src.txt", "r") as src:
        
        #Kaynak dosyası ("optab.txt") okuma modunda açıldı.
        with open("optab.txt", "r") as optab:
            
              # Ara dosya ("intermediate.txt") yazma modunda açıldı
            with open("intermediate.txt", "w") as intermediate:#intermediate, programın ilerleyişi sırasında üretilen geçici çıktıları içerir. 
                
                # Sembol tablosu dosyası ("symtab.txt") yazma modunda açıldı
                with open("symtab.txt", "w") as symtab:
                    
                    pos = 0 #Dosya konumu için başlangıç değeri belirlendi
                    
                    
                    while True:
                        line, pos = read_line_from_file(src, pos) # Dosyadan bir satır okunarak ve dosya konumu güncellenerek "line" ve "pos" değişkenlerine atandı.
                        if not line:#Eğer okunan satır boş ise
                            break #Döngüyü kır
                        
                         # Okunan satır parçalandı ve etiket, opcode, operand ve geri kalan kısımlar ayrı değişkenlere atandı.
                        label, opcode, operand, rest = break_line(line)
                        
                        #Eğer opcode "START" ise
                        if opcode == "START":
                            #Başlangıç adresi,verilen operand güncellendi veya operan yoksa sıfır olarak bırakıldı.
                            startaddress = int(operand, 16) if operand else 0
                            locctr = startaddress#Locctr,başlangıç adresine eşitlendi.
                            progname = label#Program ismi, verilen etişket ile güncelendi.
                            
                            #ara dosyaya başlangıç verileri yazıldı.
                            intermediate.write(f"{locctr:04X}\t{label}\t{opcode}\t{operand}\n")  # Onaltılık sayı formatına dönüştürme eklendi
                            continue
                        
                        #Eğer opcode "END" ise:
                        elif opcode == "END":
                            break
                        
                        #Eğer etiket varsa ve etiket nokta ile başlamıyorsa
                        if label and label[0] != '.':
                            
                            #Eğer sembol tablosunda bulunuyorsa
                            if search_symtab(label):
                                print("Hata: Symtable'da Bulundu") 
                            else:
                                symtab.write(f"{label}\t{locctr:04X}\n")  #Etiket ve locctr değeri satır bilgileri yazıldı.

                        intermediate.write(f"{locctr:04X}\t{label}\t{opcode}\t{operand}\n")#Ara dosyaya locctr değeri ve satır bilgileri yazıldı.

                        if search_optab(opcode):#Eğer opcode optab dosyasında bulunuyorsa
                            locctr += 3 #Locctr 3 artıldı.
                            
                        elif opcode == "WORD":#Eğer opcode "WORD" ise:
                            locctr += 3 #Locctr değeri üç arttırıldı.
                            
                        elif opcode == "RESW":#Eğer opcode "RESW" ise:
                            locctr += int(operand) * 3 # Locctr değeri, operand ile çarpılıp üç ile arttırıldı
                            
                        elif opcode == "RESB":# Eğer opcode "RESB" ise
                            locctr += int(operand) # Locctr değeri, operand ile değiştirildi
                            
                        elif opcode == "BYTE":# Eğer opcode "BYTE" ise
                            if operand[0] == 'C':#oprandın ilk karakteri "C" ise:
                                #-3 'C' karakteri uzunluk hesabına dahil olması engellendi.
                                                                          #Karakter uzunluğu
                                locctr += len(operand) - 3# Locctr değeri, operandin uzunluğundan üç çıkarıldı 
                           
                           
                            #  Operandın uzunluğundan 3 çıkarılır çünkü başta ve sonda bulunan 'X' işaretleri ve tek tırnaklar operandın uzunluğunu temsil etmez.
                            # Geriye kalan değerin yarısı, hexadecimal ifadenin bayt cinsinden uzunluğunu temsil eder. Her bir hexadecimal karakter 4 bit yer kaplar ve bu nedenle iki karakter bir baytı temsil eder.
                            # Dolayısıyla, bu değer locctr değerine eklenerek doğru adreslemeyi sağlar
                            elif operand[0] == 'X':# Operandin ilk karakteri "X" ise
                                locctr += (len(operand) - 3) // 2 # Locctr değeri, operandin uzunluğundan üç çıkarıldı ve ikiye bölündü 
                            else:
                                print("Hata: Geçersiz işlenene sahip BYTE")

                    proglength = locctr - startaddress # Program uzunluğu, locctr'den başlangıç adresi çıkarılarak hesaplandı
                    print(f"Ara dosya olusturuldu. Program adi={progname} and Program uzunlugu={hex(proglength)}")
                    
                    
                    with open("Details.txt", "w") as intermediate:
                        intermediate.write(f"{progname}\n{startaddress:04X}\n{proglength:04X}\n")  # Onaltılık sayı formatına dönüştürme eklendi

                        

if __name__ == "__main__":
    main()
