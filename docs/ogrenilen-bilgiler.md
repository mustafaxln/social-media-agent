# Öğrenilen Bilgiler

| Tarih | Konu | Not |
|-------|------|-----|
| Haz–Tem 2026 | Docker + n8n | `docker compose up -d`; veri `n8n_data` volume'da; credential'lar instance'ta |
| Tem 2026 | AI Agent | System + User + Structured Output; Memory/Tool bu projede boş |
| Tem 2026 | Model | `gpt-4o-mini` yeterli ve ucuz |
| Tem 2026 | AI çıktısı | Bazen `$json.output` altında; Code'da `item.output \|\| item` |
| Tem 2026 | Data Table | Insert row mapping; status `waiting_approval` |
| Tem 2026 | Duplicate | **If row doesn't exist** > Get Row + IF (veri taşır) |
| Tem 2026 | Item referansı | `$('Node').first()` = o node'un ilk item'ı (çok item varsa tehlikeli); Limit(1) sonrası `.first()` güvenli |
| Tem 2026 | Telegram | Bot + grup; Chat ID negatif; mesajı Code'da üret |
| Tem 2026 | Human-in-the-loop | Telegram taslak + manuel onay; status tabloda bekler |
| Tem 2026 | RSS | Webrazzi feed; alan map: title, description, url, published_at, source_name |
| Tem 2026 | Platform seçimi | WF-1: Set'te elle; WF-2: AI içeriğe göre LinkedIn/Instagram |
| Tem 2026 | Error Trigger | Ana WF Settings'te bağla + error WF Active; payload `execution.*` / `workflow.*` |
| Tem 2026 | Retry | Node Settings → Retry On Fail (3 × 2000 ms) — AI, Telegram, RSS |
| Tem 2026 | Hashtag | Tire ve Türkçe özel karakter kullanma |
| Tem–Tem 2026 | Buffer | GraphQL createPost; IG için type=post; Free 3 kanal / 10 kuyruk |
| Tem 2026 | Cloudinary | ImgBB yerine unsigned upload; secure_url |
| Tem 2026 | 2 kademeli onay | Taslak onay → görsel → final onay → yayın |
| Tem 2026 | İnsan fallback | Kötü görsel/taslak Telegram Reddet/İptal |
| Tem 2026 | cloudflared | Local Telegram Trigger için HTTPS; WEBHOOK_URL + docker restart |

## Kavramlar (pratik karşılık)

| Kavram | Bu projedeki karşılığı |
|--------|------------------------|
| Human-in-the-loop | Telegram taslak → insan okur/onaylar |
| Retry | Geçici API/Telegram hatalarında otomatik tekrar |
| Fail-safe | WF-03 Error Handling |
| Duplicate control | `source_url` ile tekrar üretimi engelleme |
| Structured output | AI'dan sabit JSON şema |
