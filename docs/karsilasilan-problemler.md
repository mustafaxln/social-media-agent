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

## Özet

En çok takıldığımız konular: **n8n item taşıma**, **Duplicate sırası**, **Error Trigger**, **local Telegram webhook (HTTPS)**.
