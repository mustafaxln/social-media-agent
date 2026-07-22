# Sistem Dokümantasyonu — Sosyal Medya İçerik Ajansı

> **Durum:** Final / Tamamlandı (Temmuz 2026)  
> **Kapsam:** Telegram `/yeni` ile manuel üretim + RSS → 2 kademeli onay → görsel → Buffer yayın + error handling  
> **Yeniden çalıştırma:** [`calisma-notlari/projeyi-yeniden-calistirma.md`](./calisma-notlari/projeyi-yeniden-calistirma.md)

---

## 1. Proje özeti

n8n tabanlı otomasyon; n8n UI’ya günlük giriş gerekmez.

1. **Manuel içerik:** Bota **DM** ile `/yeni` (platform, konu, hedef, ton) → WF-04 → WF-01  
2. **RSS içerik:** WF-02 (Webrazzi) Schedule/Manual → AI platform seçer  
3. Data Table’a kayıt (`waiting_approval`)  
4. **Grupta** taslak + **Onayla / Reddet**  
5. Onay → görsel (gpt-image-1-mini) → Cloudinary → `image_url`  
6. Final önizleme + **Yayınla / İptal**  
7. Yayınla → Buffer → LinkedIn veya Instagram → `published`  
8. Hata → WF-03 → `social_media_errors` + Telegram HATA  

**Hedef kitle:** E-ticaret markaları · **Ton:** Profesyonel ve öğretici  

---

## 2. Mimari (final)

```
Telegram DM: /yeni ──┐
                     ├──► WF-04 (tek Telegram Trigger)
WF-02 RSS ───────────┘         │
                               ├─ route=yeni → Parse → Execute → WF-01
                               └─ route=callback → onay/görsel/Buffer
WF-01: AI → Insert → Grup taslak [Onayla|Reddet]
         │
         ▼
   waiting_approval → approved → image → FINAL [Yayınla|İptal] → published
         │
         └── hata → WF-03
```

**Kritik kural:** Aynı botta **tek** Telegram Trigger (WF-04). İkinci Trigger webhook çakışması yaratır.

---

## 3. Workflow’lar

| ID | Ad | Tetikleyici | Görev |
|----|-----|-------------|--------|
| WF-01 | Manuel İçerik Üretme | **Execute Workflow** (WF-04’ten) | AI → Insert → grup taslak |
| WF-02 | Kaynaktan İçerik | Schedule + Manual | RSS → duplicate → AI → Insert → taslak |
| WF-03 | Error Handling | Error Trigger | Hata kaydı + HATA mesajı |
| WF-04 | Telegram Hub | Telegram (`message` + `callback_query`) | `/yeni` + onay/görsel/yayın |

**Error Workflow:** WF-01, WF-02, WF-04 → WF-03  

**Export’lar (repo kökü):** `WF-01…`, `WF-02…`, `WF-03…`, `WF-04 Telegram Onay.json` (güncel export önerilir)

### 3.1 WF-01 — Manuel (n8n’siz giriş)

```
When Executed by Another Workflow
  (topic, platform, target_audience, tone)
  → AI Agent (manuel-icerik-prompt)
  → Code (telegram_message)
  → Insert waiting_approval
  → Telegram grup [Onayla|Reddet]
```

**Input schema:** `topic`, `platform`, `target_audience`, `tone` (String)  
Eski Manual Trigger + Edit Fields kaldırılabilir / yedek test için tutulabilir.

### 3.2 WF-02 — Kaynak

```
Schedule/Manual → RSS → Veri Temizle
  → Duplicate (If row doesn't exist, source_url)
  → Limit(1) → AI → Code ($('Limit').first())
  → Insert → Telegram buton
```

### 3.3 WF-03 — Error

```
Error Trigger → Hata Mesaji (Code) → social_media_errors → Telegram HATA
```

### 3.4 WF-04 — Telegram hub

```
Telegram Trigger (message + callback_query)
  → Giris Ayir (Code) → route: callback | yeni | ignore
  → Switch
       ├─ callback → Callback Parse → approve/reject/publish/cancel (eski zincir)
       └─ yeni → Parse /yeni → IF ok → Execute Workflow WF-01
```

| callback_data | Sonuç |
|---------------|--------|
| `approve:ID` | approved → Image → Cloudinary → FINAL |
| `reject:ID` | rejected |
| `publish:ID` | Buffer → published |
| `cancel:ID` | preview_rejected |

Instagram Buffer: `metadata.instagram { type: post, shouldShareToFeed: true }`  
Publish sonrası Update Match: `$('Callback Parse').item.json.content_id`

---

## 4. `/yeni` kullanımı

**Nereye:** Bota **özelden (DM)** — grupta tetikleme güvenilir değil (Telegram kısıtları).  
**Taslak nereye düşer:** Sabit grup Chat ID (`-100…`).

```text
/yeni
platform: LinkedIn
konu: ...
hedef: ...
ton: Profesyonel ve öğretici
```

Pin şablonu: [`templates/telegram/yeni-komut-sablonu.md`](../templates/telegram/yeni-komut-sablonu.md)

---

## 5. Dış servisler

| Servis | Kullanım |
|--------|----------|
| OpenAI gpt-4o-mini | Metin (WF-01/02) |
| OpenAI gpt-image-1-mini | Görsel (WF-04) |
| Cloudinary | `secure_url` → image_url |
| Buffer Free GraphQL | LI/IG yayın |
| Telegram Bot | DM `/yeni`, grup onay, HATA |
| Webrazzi RSS | Kaynak |
| cloudflared quick tunnel | Local HTTPS → `WEBHOOK_URL` |

**Maliyet:** Onaylı post (metin + görsel) ≈ **0,02 – 0,03 USD**. → [`maliyet-notlari.md`](./maliyet-notlari.md)

---

## 6. Data Table

[`data-table-yapisi.md`](./data-table-yapisi.md)

`waiting_approval` → `approved` / `rejected` → (`preview_rejected`) → `published`

---

## 7. Retry / fallback

| Mekanizma | Durum |
|-----------|--------|
| WF-03 Error | ✅ WF-01/02/04 bağlı |
| Retry On Fail | ✅ kritik node’larda |
| İnsan (Reddet/İptal) | ✅ |
| Ağır otomatik fallback | ❌ sonraya |
| execution_logs insert | ❌ şema var, insert yok |

---

## 8. Local çalıştırma

Detay: [`calisma-notlari/projeyi-yeniden-calistirma.md`](./calisma-notlari/projeyi-yeniden-calistirma.md)

```bash
docker compose up -d
cloudflared tunnel --url http://localhost:5678
# .env WEBHOOK_URL=https://….trycloudflare.com/
docker compose up -d
# WF-04 Inactive → Active
```

---

## 9. Prompt’lar

| Dosya | WF |
|--------|-----|
| `prompts/manuel-icerik-prompt.md` | WF-01 |
| `prompts/kaynaktan-icerik-prompt.md` | WF-02 |

---

## 10. Bilinen sorunlar

Tam liste: [`karsilasilan-problemler.md`](./karsilasilan-problemler.md) · [`cozum-notlari.md`](./cozum-notlari.md)

Öne çıkanlar (son dönem dahil): quick tunnel URL değişimi, Switch’te `callbackQuery.id` yokluğu → `Giris Ayir`, Telegram parse entities / Attribution, `/yeni` sadece DM, duplicate sırası, Cloudinary, Buffer IG type, `content_id` referansı.

---

## 11. Sonraya

- Named Tunnel / VPS (sabit HTTPS)  
- execution_logs insert, ağır fallback  
- PM §15–16 (takvim, brand voice, multi-agent)  
- Grupta `/yeni` (privacy/admin ile hâlâ kırılgan; bilinçli DM tercihi)  

---

## 12. Doküman haritası

| Dosya | İçerik |
|--------|--------|
| Bu dosya | Ana sistem özeti |
| `calisma-notlari/projeyi-yeniden-calistirma.md` | Cold start |
| `calisma-notlari/telegram-yeni-komutu.md` | `/yeni` kurulum notu |
| `yol-haritasi-onay-gorsel-yayin.md` | Onay/görsel/yayın |
| `karsilasilan-problemler.md` / `cozum-notlari.md` | Problem & çözüm |
| `../proje-plani.md` | Faz planı |
| `../proje-tanımı.md` | PM brief |
