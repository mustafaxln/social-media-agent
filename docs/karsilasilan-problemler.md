# Karşılaşılan Problemler

Proje boyunca takıldığımız noktalar. Çözümler → [`cozum-notlari.md`](./cozum-notlari.md)

| # | Tarih | Faz | Problem | Etki |
|---|-------|-----|---------|------|
| 1 | Tem 2026 | 3 | Telegram **kanal**ına bot mesaj atamıyor (admin / izin) | Bildirim kurulumu tıkanıyor |
| 2 | Tem 2026 | 3 | Data Table Insert sonrası `$json.telegram_message` undefined | Telegram boş / hata |
| 3 | Tem 2026 | 3 | Expression alanında `={{ }}` kullanımı → invalid syntax | Node çalışmıyor |
| 4 | Tem 2026 | 3 | `impact_score` metin/`/5` ile kaydedilmeye çalışılınca tip uyumsuzluğu | Insert hatası veya yanlış veri |
| 5 | Tem 2026 | 3 | Telegram mesajında "sent automatically with n8n" footer | Profesyonel görünmüyor |
| 6 | Tem 2026 | 4 | Duplicate için **Get Row**: eşleşme yoksa boş output; Always Output açıkken boş `{}` | IF True olsa bile RSS verisi kayboluyor |
| 7 | Tem 2026 | 4 | Limit **önce**, Duplicate **sonra** | Hep aynı (ilk) haber deneniyor; yeni haberler işlenmiyor |
| 8 | Tem 2026 | 4 | Code'da `$('Veri Temizle').first()` | İçerik değişiyor, **link hep 1. haber**; duplicate bozuluyor |
| 9 | Tem 2026 | 4 | `#E-ticaret` gibi tireli hashtag | Telegram/sosyal medyada hashtag bölünüyor |
| 10 | Tem 2026 | 4 | Prompt'ta "WF-1 ile uyumlu..." geliştirici notu | AI için anlamsız; kafa karıştırıyor |
| 11 | Tem 2026 | 5 | WF-03 bağlı/aktif değilken ana workflow hata alıyor ama error WF tetiklenmiyor | Hata kaydı ve Telegram HATA yok |
| 12 | Tem 2026 | 5 | Set node ile nested Error Trigger alanları (`node`, `error.message`) boş | Telegram'da Node/Hata satırları boş |
| 13 | Tem 2026 | 5 | Telegram Text'te `$('Hata Bilgileri')` → Referenced node doesn't exist | Expression node adı uyuşmuyor |
| 14 | Tem 2026 | 5 | Code satırı yanlışlıkla Telegram Text'e yazılınca | Telegram'a literal `const source = ...` gidiyor |
| 15 | Tem 2026 | A | Telegram Trigger Active: `bad webhook: An HTTPS URL must be provided` | WF-04 publish edilemiyor |
| 16 | Tem 2026 | 4+ | ImgBB Internal upload error / limit | Görsel URL kaydı kırılıyor |
| 17 | Tem 2026 | 4+ | Instagram Buffer: type (post/story/reel) zorunlu | createPost reddediliyor |
| 18 | Tem 2026 | 4+ | Publish sonrası Update: `$json.content_id` undefined | status published olmuyor |
| 19 | Tem 2026 | 4+ | cloudflared quick tunnel kapanınca / URL değişince Onayla çalışmıyor | WF-04 webhook ölü URL'ye bakıyor |
| 20 | Tem 2026 | /yeni | Switch: `callbackQuery.id` exists tutmuyor | Callback dalı hiç çalışmıyor |
| 21 | Tem 2026 | /yeni | Trigger'da yalnız `callback_query` iken `/yeni` execution açmıyor | Manuel giriş tetiklenmiyor |
| 22 | Tem 2026 | /yeni | Aynı botta 2. Telegram Trigger uyarısı / riski | Webhook çakışması |
| 23 | Tem 2026 | /yeni | `can't parse entities` (byte offset …) Send Message | Taslak Telegram'a gitmiyor |
| 24 | Tem 2026 | /yeni | `/yeni` DM'de çalışıyor, **grupta** tetiklenmiyor | Grupta manuel giriş yok |

## Özet (temalar)

1. **n8n veri taşıma** — Insert sonrası alan kaybı, `$('Node').first()`, HTTP sonrası `$json` ezilmesi  
2. **RSS duplicate** — sıra ve doğru source node  
3. **Local Telegram** — HTTPS tunnel, tek Trigger, `message`+`callback_query`, URL yenileme  
4. **Payload şekli** — callback çoğu zaman kökte `data` (nested `callbackQuery` yok)  
5. **Görsel / yayın** — ImgBB→Cloudinary, Buffer IG metadata  
6. **UX** — Parse Mode / Attribution entity hatası; grup vs DM  

## Dönemsel hikâye (kısa)

- **Faz 2–3:** Manuel AI + Data Table + Telegram grup; kanal yerine grup.  
- **Faz 4:** RSS + duplicate tuzakları.  
- **Faz 5:** Error WF bağlama ve Code ile hata parse.  
- **Faz A–D:** Buton onayı, tunnel, görsel, Buffer.  
- **Final UX:** PM isteği → n8n Edit Fields yerine `/yeni` DM; WF-04 hub.  
