# Sistem Dokümantasyonu — Sosyal Medya İçerik Ajansı

> **Durum:** Tamamlandı (Temmuz 2026)  
> **Kapsam:** Üretim → 2 kademeli Telegram onayı → görsel → Buffer ile LinkedIn/Instagram yayın + error handling  
> **Not:** Bu dosya projenin uçtan uca teknik özetidir. Workflow dosyalarına dokunulmadan yazılmıştır.

---

## 1. Proje özeti

n8n tabanlı otomasyon:

1. **Manuel** konu veya **RSS** (Webrazzi) ile içerik fikri alır  
2. AI ile LinkedIn / Instagram post taslağı üretir  
3. Data Table’a kaydeder (`waiting_approval`)  
4. Telegram’a taslak + **Onayla / Reddet** gönderir  
5. Onayda görsel üretir (OpenAI Image mini) → Cloudinary URL  
6. Final önizleme (foto + metin) + **Yayınla / İptal**  
7. Yayınla → Buffer → LinkedIn veya Instagram → `published`  
8. Hatalar → WF-03 → `social_media_errors` + Telegram HATA  

**Hedef kitle:** E-ticaret markaları  
**Ton:** Profesyonel ve öğretici  

---

## 2. Mimari

```
┌─────────────┐     ┌─────────────┐
│ WF-01 Manuel│     │ WF-02 RSS   │
│ konu+platform│     │ Schedule/   │
│ (biz seçer) │     │ Manual      │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └─────────┬─────────┘
                 ▼
    social_media_contents (waiting_approval)
                 ▼
         Telegram taslak [Onayla|Reddet]
                 ▼
┌────────────────────────────────────────┐
│ WF-04 Telegram Onay / Görsel / Yayın   │
│  reject → rejected                     │
│  approve → Image → Cloudinary → FINAL  │
│            Telegram [Yayınla|İptal]    │
│  cancel → preview_rejected             │
│  publish → Buffer → LI/IG → published  │
└────────────────────────────────────────┘
                 │ (hata)
                 ▼
         WF-03 Error Handling
         → social_media_errors + Telegram HATA
```

---

## 3. Workflow’lar

| ID | Ad | Tetikleyici | Görev |
|----|-----|-------------|--------|
| WF-01 | Manuel İçerik Üretme | Manual | Konu + platform → AI → Insert → Telegram buton |
| WF-02 | Kaynaktan İçerik Üretme | Schedule + Manual | RSS → duplicate → Limit → AI → Insert → Telegram buton |
| WF-03 | Error Handling | Error Trigger | Hata kaydı + Telegram HATA |
| WF-04 | Telegram Onay / Yayın | Telegram Callback | Onay, görsel, Buffer yayın |

**Error Workflow bağları:** WF-01, WF-02, WF-04 → WF-03  

**Export dosyaları (repo kökü):**  
`WF-01 …json`, `WF-02 …json`, `WF-03 …json`  
(WF-04 güncel export kullanıcı tarafından eklenmeli)

### 3.1 WF-01 akış

```
Manual Trigger → Set (topic, platform, …)
  → AI Agent (manuel-icerik-prompt)
  → Code (telegram_message)
  → Insert (waiting_approval)
  → Telegram (metin + approve:ID / reject:ID)
```

Platform **kullanıcı** seçer.

### 3.2 WF-02 akış

```
Schedule/Manual → RSS (webrazzi.com/feed)
  → Veri Temizle → Duplicate (If row doesn't exist, source_url)
  → Limit(1) → AI (kaynaktan-icerik-prompt; platform AI)
  → Code ($('Limit').first() ile source_url)
  → Insert → Telegram buton
```

### 3.3 WF-03 akış

```
Error Trigger → Hata Mesaji (Code) → Insert social_media_errors → Telegram HATA
```

### 3.4 WF-04 akış (callback_data)

| data | Davranış |
|------|----------|
| `approve:ID` | status=approved → Image → Cloudinary → final Telegram |
| `reject:ID` | status=rejected |
| `publish:ID` | Get row → Buffer createPost → status=published |
| `cancel:ID` | status=preview_rejected |

Instagram Buffer: `metadata.instagram.type = post`, `shouldShareToFeed = true`  
Update Match (publish sonrası): `$('Callback Parse').item.json.content_id`

---

## 4. Dış servisler

| Servis | Kullanım | Not |
|--------|----------|-----|
| OpenAI gpt-4o-mini | Metin | WF-01/02 |
| OpenAI gpt-image-1-mini | Görsel | medium; prompt’ta yazı yasak |
| Cloudinary | image_url | Unsigned upload preset |
| Buffer Free | LI/IG yayın | GraphQL `https://api.buffer.com` |
| Telegram Bot | Taslak / final / HATA | Grup; inline buton |
| Webrazzi RSS | Kaynak | `https://webrazzi.com/feed` |
| cloudflared | Local webhook HTTPS | `WEBHOOK_URL` in `.env` |

---

## 5. Data Table

Detay: [`data-table-yapisi.md`](./data-table-yapisi.md)

**Status:** `waiting_approval` → `approved` / `rejected` → (`preview_rejected`) → `published`  

**Kritik sütunlar:** `id` (callback), `platform`, `image_url`, `source_url`, `status`

---

## 6. Retry / fallback (PM §12–13)

| Mekanizma | Uygulama |
|-----------|----------|
| Error WF | WF-03 + WF-01/02/04 bağlı |
| Retry On Fail | Image, Cloudinary, Buffer, Telegram, AI, RSS |
| İnsan fallback | Reddet / İptal (kötü taslak veya görsel) |
| Ağır fallback | Yedek RSS / template — yok (bilinçli) |
| execution_logs insert | Yok (şema var) |

---

## 7. Local kurulum hatırlatması

```bash
docker compose up -d
# Telegram Trigger için:
cloudflared tunnel --url http://localhost:5678
# .env WEBHOOK_URL=https://….trycloudflare.com/
docker compose up -d
```

n8n: http://localhost:5678 — detay: [`calisma-notlari/n8n-kurulum.md`](./calisma-notlari/n8n-kurulum.md)

---

## 8. Prompt dosyaları

| Dosya | Kullanım |
|--------|----------|
| `prompts/manuel-icerik-prompt.md` | WF-01 |
| `prompts/kaynaktan-icerik-prompt.md` | WF-02 |

Görsel prompt (WF-04): yazı/logo yok; `visual_idea` + platform.

---

## 9. Bilinen sorunlar ve çözümler

Tam liste: [`karsilasilan-problemler.md`](./karsilasilan-problemler.md) · [`cozum-notlari.md`](./cozum-notlari.md)

Öne çıkanlar: duplicate sırası, `$('Limit').first()`, HTTPS webhook, Cloudinary (ImgBB limit), Instagram Buffer `type`, publish sonrası `content_id` referansı.

---

## 10. Sonraya bırakılanlar

- execution_logs insert  
- Ağır otomatik fallback  
- PM §15–16 (takvim, brand voice, multi-agent, …)  
- WF-04 güncel JSON export (repoya eklenmeli)  

---

## 11. Doküman haritası

| Dosya | İçerik |
|--------|--------|
| Bu dosya | Uçtan uca sistem özeti |
| `yol-haritasi-onay-gorsel-yayin.md` | Onay/görsel/yayın final akış |
| `akis-semasi.md` | Mermaid şemalar |
| `planlanan-workflow-yapisi.md` | WF tablosu |
| `calisma-notlari/` | Faz ve checkpoint notları |
| `../proje-plani.md` | Faz 0–6 plan |
| `../proje-tanımı.md` | PM orijinal brief |
