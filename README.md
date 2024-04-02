# SCI_Pass1_Python
SCİ mimarisinin pass1 algoritması referans alarak yazılmış python kodlarını içerir.

# SCİ (Superscalar Architecture) mimarisi nedir?
İşlemci performansını artırmak için birden çok talimatı aynı anda işleyebilen bir mikroişlemci mimarisidir. 

# Proje ne işe yarar?
Bu proje, assembly dilinde yazılmış kodları analiz ederek ara dosyalar oluşturan bir araç sunar. Bu ara dosyalarda, her bir komutun yerini, sembol tablosunu ve programın uzunluğunu belirten bilgiler bulunur. Bu şekilde, assembly kodlarının derlenmesi, çevrilmesi veya analiz edilmesi gibi işlemler kolaylıkla yapılabilir.

# Proje neden faydalıdır?
Proje, assembly dilinde yazılmış kodların analizini sağlayarak yazılım geliştiricilere ve sistem tasarımcılarına büyük bir kolaylık sunar. Assembly kodlarının anlaşılması ve işlenmesi karmaşık olabilir, bu araç sayesinde kodun anlaşılması ve yönetilmesi daha basit hale gelir. Ayrıca, proje sayesinde kodun hatalarını bulmak ve geliştirmek de daha kolay hale gelir.

## Nasıl Kullanılır

1. `src.txt` dosyasına analiz edilecek assembly kodu eklenir.
2. `optab.txt` dosyasına opcode tablosu eklenir.
3. Gerekirse sembol tablosu (`symtab.txt`) oluşturulur.
4. Betik çalıştırılır ve analiz işlemi gerçekleştirilir.
5. Sonuçlar, `intermediate.txt` ve `Details.txt` dosyalarında bulunabilir.

## Fonksiyonlar

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

