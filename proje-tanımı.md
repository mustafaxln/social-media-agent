Sosyal Medya İçerik Agent Projesi
Proje Amacı
Bu projenin amacı, sosyal medya içerik üretimi sürecini AI agent mantığı ile otomatikleştirmeyi öğrenmektir.
Bu çalışma kapsamında n8n, Docker, API, AI agent, prompt engineering, veri kaydı, Telegram bildirimi, hata yönetimi ve dokümantasyon konularında pratik yapılacaktır.

1. Proje Öncesi Hazırlık
1.1. Planlama Dokümanı Oluşturma
Projeye başlamadan önce Google Docs, Notion veya benzeri bir platformda proje dokümanı oluşturulmalıdır.
Dokümanda bulunması gerekenler:

Proje amacı
Kullanılacak teknolojiler
Öğrenilecek kavramlar
Planlanan workflow yapısı
Akış şeması
Data Table yapısı
Karşılaşılan problemler
Çözüm notları
Ekran görüntüleri
Öğrenilen bilgiler
1.2. Akış Şeması Hazırlama
Kodlamaya veya workflow kurulumuna başlamadan önce sistemin genel akışı çizilmelidir.
Örnek akış:
İçerik Kaynağı
↓
Veri Çekme
↓
Duplicate Kontrolü
↓
AI Agent ile İçerik Üretimi
↓
Data Table Kaydı
↓
Telegram'a Taslak Gönderimi
↓
Onay Süreci
↓
Yayın / Arşiv2. Docker ile Local n8n Kurulumu

3. Proje Senaryosunu Belirleme
Bu projede amaç, belirlenen kaynaklardan sosyal medya içerik fikirleri üretmek ve bunları AI agent ile sosyal medya formatına dönüştürmektir.
3.1. Hangi platformlar desteklenecek?
İlk aşamada en az 2 platform seçilmelidir.
Örnek platformlar:

LinkedIn
Instagram
X / Twitter
TikTok
YouTube Shorts
Blog
Newsletter


3.2. İçerik türleri belirlenmeli
Örnek içerik türleri:

Eğitici içerik
Duyuru
Kampanya
Ürün tanıtımı
Trend yorumu
Haber yorumu
İpucu / mini rehber
Problem / çözüm
Liste içerik
Soru-cevap
Case study
Mizahi içerik
Topluluk etkileşimi


4. İçerik Kaynaklarını Belirleme
Agent’ın içerik üretirken kullanacağı kaynaklar belirlenmelidir.
4.1. Kaynak örnekleri

RSS haber kaynakları
Blog yazıları
Web siteleri
Google Trends
Rakip sosyal medya hesapları
Ürün dokümanları
Marka dokümanları
YouTube video başlıkları
LinkedIn post fikirleri
X / Twitter gündem konuları


5. n8n Workflow 1: Manuel İçerik Üretme
İlk aşamada dış kaynaktan veri çekmeden, manuel girilen bir konu üzerinden içerik üreten workflow yapılmalıdır.
5.1. Amaç
Kullanıcı bir konu girer, AI agent bu konuya göre sosyal medya içeriği üretir.
5.2. Workflow akışı
Manual Trigger
↓
Set Node
↓
AI Agent / Chat Model
↓
Structured Output
↓
Data Table Kaydı
↓
Telegram Bildirimi5.3. Set Node örnek alanları
{
  "topic": "E-ticarette yapay zeka kullanımı",
  "platform": "LinkedIn",
  "target_audience": "E-ticaret markaları",
  "tone": "Profesyonel ve öğretici"
}5.4. AI çıktısı
AI agent aşağıdaki alanları üretmelidir:

Başlık
İçerik metni
Platform
Hedef kitle
İçerik kategorisi
Hashtagler
CTA
Görsel fikri
Ton
Etki skoru


6. Prompt Tasarımı
AI agent için kullanılacak prompt dikkatli hazırlanmalıdır.
6.1. Örnek prompt
Sen bir sosyal medya içerik stratejisti gibi çalışıyorsun.

Görevin, verilen konuya göre platforma uygun sosyal medya içeriği üretmek.

Kurallar:
- İçerik hedef kitleye uygun olmalı.
- Platform diline uygun yazılmalı.
- Gereksiz uzun olmamalı.
- Satış odaklı değil, değer odaklı olmalı.
- Hashtag önerileri eklenmeli.
- CTA bulunmalı.
- Görsel fikri verilmeli.
- Çıktı JSON formatında olmalı.6.2. Örnek JSON çıktı
{
  "title": "E-ticarette Yapay Zeka ile Daha Akıllı Müşteri Deneyimi",
  "platform": "LinkedIn",
  "category": "Eğitici içerik",
  "target_audience": "E-ticaret markaları",
  "content": "Yapay zeka artık sadece otomasyon için değil, müşteri deneyimini kişiselleştirmek için de kullanılıyor...",
  "hashtags": ["#eticaret", "#yapayzeka", "#müşterideneyimi"],
  "visual_idea": "Müşteri yolculuğu üzerinde AI öneri noktalarını gösteren sade bir görsel",
  "cta": "Siz e-ticaret süreçlerinizde yapay zekayı nasıl kullanıyorsunuz?",
  "tone": "Profesyonel ve öğretici",
  "impact_score": 4
}

7. n8n Data Table Yapısı
Üretilen içerikler Data Table’a kaydedilmelidir.
7.1. Content Table
Oluşturulacak tablo adı:
social_media_contents

7.2. Status alanı
Önerilen durumlar:

draft
waiting_approval
approved
rejected
scheduled
published
failed


8. Telegram Bildirimi
Üretilen içerikler Telegram kanalına gönderilmelidir.
Yeni Sosyal Medya İçerik Taslağı Platform: LinkedIn Kategori: Eğitici İçerik Hedef Kitle: E-ticaret Markaları Etki Skoru: 4/5 Başlık: ... İçerik: ... Hashtagler: ... Görsel Fikri: ... CTA: ... Durum: Onay bekliyor
9. Onay Süreci
Sosyal medya içerikleri doğrudan yayınlanmamalıdır. Önce onaya gönderilmelidir.
9.1. İlk aşama
İlk aşamada içerik sadece Telegram’a taslak olarak gönderilir.
Kişi manuel olarak içeriği kontrol eder.
9.2. İleri aşama
Daha sonra onay mekanizması eklenebilir.
Onay yöntemleri:

Telegram üzerinden butonlu onay
n8n Form ile onay
Google Sheet üzerinden status değiştirme
Data Table’da approval_status alanını güncelleme
9.3. Öğrenilecek kavramlar

Human-in-the-loop nedir?
Approval workflow nedir?
State management nedir?
Status tracking nedir?


10. n8n Workflow 2: Kaynaktan İçerik Üretme
Bu aşamada dış kaynaklardan içerik çekilmelidir.
10.1. Workflow akışı
Schedule Trigger
↓
RSS Feed / HTTP Request
↓
Veri Temizleme
↓
Duplicate Kontrolü
↓
AI Agent
↓
Data Table Kaydı
↓
Telegram Bildirimi10.2. Kaynaklardan çekilecek alanlar

Başlık
Açıklama
URL
Yayın tarihi
Kaynak adı
10.3. Duplicate kontrolü
Aynı içerik tekrar üretilmemelidir.
Duplicate kontrol yöntemleri:

URL kontrolü
Title kontrolü
URL + title hash kontrolü
Data Table’da daha önce var mı kontrolü


11. AI ile Sınıflandırma
Agent çekilen içerikleri sınıflandırmalıdır.
11.1. Sosyal medya içerik kategorileri

Eğitici içerik
Haber yorumu
Trend yorumu
Kampanya
Ürün tanıtımı
Problem / çözüm
İpucu
Liste içerik
Case study
Soru-cevap
11.2. Platform seçimi
Agent içeriğe göre uygun platform önerebilir.
Örnek:
Bu içerik LinkedIn için mi daha uygun, Instagram için mi, X/Twitter için mi?

12. Error Handling Workflow
Hatalar ayrı bir workflow ile yönetilmelidir.
12.1. Error workflow akışı
Error Trigger
↓
Hata Bilgilerini Alma
↓
Error Data Table Kaydı
↓
Telegram Error Kanalına Bildirim

13. Retry ve Fallback Senaryoları
Workflow hata aldığında tamamen durmamalıdır.
13.1. Retry senaryoları

API geçici olarak cevap vermezse tekrar dene
Telegram mesajı gönderilemezse tekrar dene
AI çıktısı bozuk gelirse tekrar prompt gönder
RSS kaynağı boş dönerse alternatif kaynağa geç
13.2. Fallback senaryoları

Ana kaynak çalışmazsa yedek kaynak kullan
AI agent başarısız olursa basit template ile içerik üret
Telegram başarısız olursa Data Table’a telegram_failed olarak kaydet
13.3. Öğrenilecek kavramlar

Retry nedir?
Timeout nedir?
Fallback nedir?
Exponential backoff nedir?
Fail-safe workflow nedir?


14. Loglama ve Monitoring
Projenin takip edilebilir olması gerekir.
14.1. Takip edilecek metrikler

Kaç kaynak kontrol edildi?
Kaç içerik üretildi?
Kaç içerik Telegram’a gönderildi?
Kaç içerik onay bekliyor?
Kaç hata oluştu?
En çok hata alan node hangisi?
En çok içerik üreten kaynak hangisi?
14.2. Log tablosu
Tablo adı:
social_media_execution_logsSütunlar:

id
workflow_name
execution_id
total_sources
generated_contents
sent_to_telegram
failed_count
started_at
finished_at
status






15. Gelişmiş Özellikler
İlk versiyon tamamlandıktan sonra aşağıdaki özellikler eklenebilir.
15.1. İçerik Takvimi

Haftalık içerik planı üretme
Platform bazlı yayın günü önerisi
İçerik yoğunluğu kontrolü
Data Table’da yayın tarihi tutma
15.2. Rakip Analizi

Rakip hesapların içeriklerini analiz etme
Kullanılan konu başlıklarını çıkarma
Hashtag analizi yapma
En çok etkileşim alan içerik formatlarını belirleme
15.3. Brand Voice

Marka tonu oluşturma
Yasaklı kelimeler listesi
Emoji kullanım kuralları
Kurumsal dil kontrolü
İçerik kalite kontrolü
15.4. Görsel Brief Üretimi
Agent sadece metin değil, görsel fikri de üretmelidir.
Örnek çıktılar:

Instagram carousel fikri
Canva tasarım brief’i
Görsel açıklaması
Slide başlıkları
Görsel boyut önerisi
AI image prompt’u
15.5. İçeriği Yeniden Kullanma
Tek bir içerikten farklı platformlara uygun içerikler üretilebilir.
Örnekler:

Blog yazısından LinkedIn postu
LinkedIn postundan Instagram carousel
Haberden X/Twitter thread
Videodan kısa açıklama
Newsletter’dan sosyal medya postu






16. Multi-Agent Yapısı
İleri seviye olarak proje multi-agent yapıya dönüştürülebilir.
16.1. Agent rolleri

Research Agent: Kaynakları araştırır.
Content Writer Agent: İçeriği yazar.
Editor Agent: Yazım ve ton kontrolü yapar.
Classification Agent: İçeriği sınıflandırır.
Compliance Agent: Marka kurallarına uygunluğu kontrol eder.
Publisher Agent: Onaylanan içeriği yayına hazırlar.
Analytics Agent: Performans verilerini analiz eder.
16.2. Öğrenilecek kavramlar

Multi-agent nedir?
Agent görev ayrımı nedir?
Tool kullanımı nedir?
Memory nedir?
RAG nedir?
LangChain nedir?
LangGraph nedir?






17. Beklenen Final Çıktılar
Proje sonunda aşağıdaki çıktılar beklenmektedir:

Docker ile local çalışan n8n kurulumu
Docker Compose dosyası
Manuel içerik üretim workflow’u
Kaynaktan içerik üretim workflow’u
Error handling workflow’u
Data Table yapıları
Telegram bildirim sistemi
En az 2 platform için içerik üretimi
Duplicate kontrolü
Retry / fallback senaryosu
Proje dokümantasyonu
Akış şeması
Ekran görüntüleri
Öğrenilen kavramlar listesi
Karşılaşılan problemler ve çözümler


--------------------------------

Ekstra maddeler 

bu projede adım adım gidelim

sosyal medya platformlarında api ile içerik üretebiliyor muyuz ? Görsel, Video, Yazı ?Üretilecek içerikleri hazırlayacak ai karşılaştırmaları ? 
içerik üretebildiğimiz platformların api kullanım dökümanları, kısıtları, ücretleri, api key almak için gerekli adımlar platform platform ?
demo hesaplar ile manuel içerik üretimi 
ai ile içerik üretimi
telegram onayı ile içerik üretimi
her adımda görüşelim.[3:02 PM]
mevut buna benzer projelerin araştırılması ?
benzer projelerin yetenekleri ?
benzer projelerde open source olanlar varsa test edilip n8n ile karşılaştırılması?