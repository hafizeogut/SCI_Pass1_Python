# SCI_Pass1_Python
SCİ mimarisinin pass1 algoritması referans alarak yazılmış python kodlarını içerir.

# SCI (Superscalar Architecture) mimarisi nedir?

![Resim2](https://github.com/hafizeogut/SCI_Pass1_Python/assets/94183443/dfc45c0b-89c4-43b1-beb1-5d1ce886d3de)


İşlemci performansını artırmak için birden çok talimatı aynı anda işleyebilen bir mikroişlemci mimarisidir. 

# Proje ne işe yarar?
Bu proje, assembly dilinde yazılmış kodları analiz ederek ara dosyalar oluşturan bir araç sunar. Bu ara dosyalarda, her bir komutun yerini, sembol tablosunu ve programın uzunluğunu belirten bilgiler bulunur. Bu şekilde, assembly kodlarının derlenmesi, çevrilmesi veya analiz edilmesi gibi işlemler kolaylıkla yapılabilir.

# Proje içerği:
![proje drawio](https://github.com/hafizeogut/SCI_Pass1_Python/assets/94183443/298f9f11-f89b-48db-b52b-d49145b01569)


# Proje neden faydalıdır?
Proje, assembly dilinde yazılmış kodların analizini sağlayarak yazılım geliştiricilere ve sistem tasarımcılarına büyük bir kolaylık sunar. Assembly kodlarının anlaşılması ve işlenmesi karmaşık olabilir, bu araç sayesinde kodun anlaşılması ve yönetilmesi daha basit hale gelir. Ayrıca, proje sayesinde kodun hatalarını bulmak ve geliştirmek de daha kolay hale gelir.

## Nasıl Kullanılır

1. `src.txt` dosyasına analiz edilecek assembly kodu eklenir.
2. `optab.txt` dosyasına opcode tablosu eklenir.
3. Gerekirse sembol tablosu (`symtab.txt`) oluşturulur.
4. Betik çalıştırılır ve analiz işlemi gerçekleştirilir.
5. Sonuçlar, `intermediate.txt` ve `Details.txt` dosyalarında bulunabilir.

## Fonksiyonlar
![sci_fonction drawio](https://github.com/hafizeogut/SCI_Pass1_Python/assets/94183443/2c50cf61-528a-4d87-b4df-9fd9dc072708)

### hexadecimal_to_decimal(x)

Verilen bir onaltılık sayıyı onluk sayıya dönüştürür.

### read_line_from_file(src, pos)

Belirtilen dosyadan belirli bir konumdan itibaren bir satır okur.

### break_line(line)

Verilen bir satırı parçalar ve etiket, opcode, operand ve geri kalan kısımları döndürür.

### search_symtab(label)

Verilen bir etiketin sembol tablosunda bulunup bulunmadığını kontrol eder.

### search_optab(opcode)

Verilen bir opcode'un opcode tablosunda bulunup bulunmadığını kontrol eder.

### main()

Ana işlemlerin gerçekleştirildiği fonksiyon. Kaynak dosyayı analiz eder, sembol tablosunu ve geçici dosyayı oluşturur ve sonuçları raporlar.

