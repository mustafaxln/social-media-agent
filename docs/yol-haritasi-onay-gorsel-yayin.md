# Yol Haritası — Onay + Görsel + Yayın

> **Durum:** Uygulamada — Faz A (Telegram buton onayı)  
> **Kaynak:** PM görüşmesi (Tem 2026) + manuel hat genişletmesi  
> **Bağımlılık:** Mevcut ilk versiyon (WF-01 / WF-02 / WF-03) üzerine inşa  
> **Kural:** Her başarılı fazdan sonra doğrulama → git commit (geri dönüş noktası)

Bu dosya, Telegram buton onayı, görsel üretimi ve LinkedIn/Instagram yayınını kapsayan **sonraki aşama** planıdır. Hem **kaynaktan (RSS)** hem **manuel konu** hattını kapsar. İlk versiyon dokümantasyonundan (`proje-plani.md`) ayrı tutulur.

---

## İki giriş, tek onay/yayın hattı

```
┌─ A) MANUEL (WF-01) ─────────────────────────┐
│  Konu + platform (biz gireriz)                │
│       ↓                                       │
│  AI → o platform için post taslağı            │
└──────────────────┬────────────────────────────┘
                   │
                   ▼
         Insert (waiting_approval)
         Telegram (taslak + Onayla / Reddet)
                   │
         ┌─────────┴─────────┐
         │ Reddet            │ Onayla
         ▼                   ▼
    status=rejected    Görsel üret
                              ↓
                       LinkedIn veya Instagram
                       (kayıttaki platform)
                              ↓
                       status=published

┌─ B) KAYNAKTAN (WF-02) ──────────────────────┐
│  RSS haber                                    │
│       ↓                                       │
│  AI → platform KARARI (LinkedIn / Instagram)  │
│       ↓                                       │
│  AI → o platform için post taslağı            │
└──────────────────┬────────────────────────────┘
                   │
                   ▼
              (aynı Telegram → onay → görsel → yayın)
```

**Onayla butonu:** Tek otomatik workflow tetiklenir → görsel üret → LinkedIn/Instagram’da paylaş.  
Kaynak fark etmez: taslak **manuel (WF-01)** veya **RSS (WF-02)** gelsin; buton aynı WF-04 hattına düşer.

**Reddet:** Sadece `status = rejected` — görsel/yayın yok.


---

## Hat A — Manuel (WF-01 düzeltme / genişletme)

**Amaç:** Biz konu (ve gerekirse kısa içerik notu) + **platformu kendimiz** gireriz; AI paylaşım için gereken postu üretir; sonra ortak onay hattına girer.

### Girdi (Set / Form)

| Alan | Kim girer | Örnek |
|------|-----------|--------|
| `topic` | Biz | "E-ticarette iade sürecini hızlandırma" |
| `platform` | Biz | `LinkedIn` veya `Instagram` |
| `target_audience` | Biz (sabit veya elle) | E-ticaret markaları |
| `tone` | Biz (sabit veya elle) | Profesyonel ve öğretici |
| `notes` (opsiyonel) | Biz | Vurgulanacak noktalar, yasaklar |

### Beklenen davranış

1. AI, **seçilen platforma** göre metin üretir (LinkedIn uzun/profesyonel; Instagram kısa/görsel odaklı).
2. Platform’u AI **değiştirmez** — Set’teki değer korunur / AI çıktısında aynı platform yazılır.
3. Code → Insert (`waiting_approval`, `source_url` boş veya `manual`) → Telegram butonlu taslak.
4. Onay sonrası: görsel → ilgili platformda yayın (Hat B ile **aynı** WF-04/05).

### WF-01’de düzeltilecekler

| # | İş | Not |
|---|-----|-----|
| M1 | Set alanlarını netleştir (`topic`, `platform` zorunlu) | İstersen n8n Form Trigger ile UI |
| M2 | Prompt: "Platform kullanıcı tarafından verildi; değiştirme" | `prompts/manuel-icerik-prompt.md` güncelle |
| M3 | Telegram mesajı butonlu hale getir | WF-02 ile aynı şablon / Code kalıbı |
| M4 | Insert sonrası ortak onay hattına bağlan | Aynı `social_media_contents` + aynı callback |

---

## Hat B — Kaynaktan (WF-02)

**Amaç:** Haber çek → AI platform seçsin → taslak → ortak onay hattı.

```
RSS → Veri Temizle → Duplicate → Limit
  → AI (platform kararı + post)
  → Code → Insert → Telegram (buton)
  → [Onay] → görsel → yayın
```

Platform burada AI’ya bırakılır; yayın IF’i kayıttaki `platform` alanına bakar.

---

## Mevcut durum vs hedef

| Adım | İlk versiyon | Bu yol haritası |
|------|--------------|-----------------|
| Manuel konu + platform | ✅ Set’te var; yayın yok | ✅ Post üret + onay + görsel + yayın |
| RSS kaynak | ✅ Schedule | ✅ Aynı + butonlu Telegram |
| Platform (manuel) | ✅ Biz seçiyoruz | ✅ Korunur, yayında kullanılır |
| Platform (RSS) | ✅ AI önerir | ✅ AI karar verir, yayında kullanılır |
| Telegram | ✅ Düz metin | ✅ Metin + **Onayla / Reddet** |
| Görsel | ❌ Sadece `visual_idea` | ✅ Onay sonrası AI image |
| Yayın | ❌ Yok | ✅ LinkedIn / Instagram |

---

## Fazlar (uygulama sırası)

### Faz A — Telegram buton onayı (ortak)

**Amaç:** Her iki hattan gelen taslaklar Onayla / Reddet ile status güncellensin.

| # | İş | Not |
|---|-----|-----|
| A1 | Telegram’a **inline keyboard** (`Onayla` / `Reddet`) | `callback_data` = content/row id |
| A2 | `WF-04 Telegram Onay` | Telegram Trigger (callback) |
| A3 | Parse → approved / rejected | |
| A4 | Data Table Update | `status` |
| A5 | (Opsiyonel) Teyit mesajı | |

**Bağımlılık:** Bot callback (webhook); grup izinleri.

---

### Faz B — Platform kuralları (iki hat farklı)

| # | İş | Not |
|---|-----|-----|
| B1 | **Manuel:** platform Set’ten gelir; AI değiştirmesin | Prompt + Code’da Set/platform override |
| B2 | **RSS:** AI yalnızca `LinkedIn` \| `Instagram` seçsin | Mevcut WF-02 prompt |
| B3 | Telegram’da platform belirgin | Yayın IF’i `platform` okur |
| B4 | Ortak yayın IF | `platform === LinkedIn` / `Instagram` |

---

### Faz C — Görsel üretimi (ortak, onay sonrası)

| # | İş | Not |
|---|-----|-----|
| C1 | Image model seçimi | OpenAI Images vb. |
| C2 | Prompt: `visual_idea` + platform oranı | |
| C3 | Saklama + `image_url` sütunu | |
| C4 | (Opsiyonel) Telegram önizleme | Varsayılan: yok, tek onay |

---

### Faz D — Sosyal medya yayını (ortak)

| # | İş | Not |
|---|-----|-----|
| D1 | LinkedIn publish | Metin + görsel |
| D2 | Instagram publish | Graph API / Business hesap |
| D3 | Onay → görsel → IF platform → publish | WF-04 veya WF-05 |
| D4 | `status = published` / hata → WF-03 | |

---

### Faz E — WF-01 + WF-02 entegrasyon ve docs

| # | İş |
|---|-----|
| E1 | WF-02 Telegram butonlu |
| E2 | WF-01 Telegram butonlu + prompt/platform kilidi |
| E3 | Export: WF-01, WF-02, WF-04 (+ WF-05) |
| E4 | Data Table + prompt + problem/çözüm docs |

---

## Önerilen hedef mimari

```
WF-01 Manuel İçerik
  Manual/Form → Set (topic + platform biz)
    → AI (o platform için post) → Code → Insert (waiting_approval)
    → Telegram (buton) ─────────────────────┐
                                            │
WF-02 Kaynaktan İçerik                      │
  Schedule/Manual → RSS → … → AI            │
    → Code → Insert → Telegram (buton) ─────┤
                                            ▼
                              WF-04 Onay (+ Yayın)
                                Callback
                                  → rejected → dur
                                  → approved
                                  → Görsel
                                  → IF platform → LinkedIn | Instagram
                                  → published
```

İki üretim workflow’u; **tek** onay/görsel/yayın workflow’u.

---

## Data Table — beklenen ekler

| Sütun | Amaç |
|-------|------|
| `image_url` | Üretilen görsel |
| `published_at` | Yayın zamanı (opsiyonel) |
| `telegram_message_id` | Callback eşleştirme (gerekirse) |
| `source_url` | RSS URL; manuelde boş veya `manual` |
| `status` | `waiting_approval` → `approved` / `rejected` → `published` / `failed` |

---

## Karar bekleyenler (uygulama başında)

1. **Görsel sağlayıcı:** OpenAI Images mi, başka mı?
2. **Instagram / LinkedIn** hesap ve API tipi
3. **Tek onay mı, görsel sonrası ikinci onay mı?** → Varsayılan: tek onay → görsel → yayın
4. **Manuel girdi:** Set mi, n8n Form mu?
5. **Uygulama sırası tercihi:** Önce ortak WF-04 mü, yoksa önce WF-01 düzeltmesi mi?

---

## Uygulama sırası (öneri)

1. **Faz A** — Ortak buton + callback + status (her iki hattın kilidi)  
2. **Faz B** — Platform kuralları (manuel kilit / RSS AI)  
3. **WF-01 + WF-02** Telegram’ı butonlu yap (Faz E1–E2 erken)  
4. **Faz C** — Görsel  
5. **Faz D** — Önce bir platform (ör. LinkedIn), sonra Instagram  
6. **Faz E** — Export + docs  

---

## Kapsam dışı

- İçerik takvimi, rakip analizi, brand voice, multi-agent (PM 15–16)  
- execution_logs insert, ağır fallback  

---

## İlişkili dosyalar

| Dosya | Rol |
|--------|-----|
| `proje-plani.md` | İlk versiyon — tamamlandı |
| `proje-tanımı.md` | PM (onay 9.2, görsel 15.4) |
| `prompts/manuel-icerik-prompt.md` | WF-01 — platform kilidi güncellenecek |
| `prompts/kaynaktan-icerik-prompt.md` | WF-02 — platform AI seçimi |
| Bu dosya | Onay + görsel + yayın (manuel + kaynak) |
