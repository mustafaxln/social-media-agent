# Bugün — Uygulama Sırası (Onay = görsel + yayın)

> **Kural:** Manuel veya RSS taslağı → Telegram’da **Onayla** → tek WF otomatik çalışır (görsel + post).  
> Her sağlam checkpoint’te doğrula → git commit.

## Hedef mimari (bugünden itibaren)

```
WF-01 Manuel  ──┐
                ├──→ Insert (waiting_approval) → Telegram [Onayla | Reddet]
WF-02 RSS     ──┘                                      │
                                                       │ callback
                                                       ▼
                                              WF-04 Onay + Yayın
                                                │
                        Reddet ─────────────────┼──→ status=rejected → DUR
                                                │
                        Onayla ─────────────────┘
                                                ▼
                                          status=approved
                                                ▼
                                          Görsel üret (AI Image)
                                                ▼
                                          IF platform
                                            → LinkedIn post
                                            → Instagram post
                                                ▼
                                          status=published
```

---

## Bugün — adım adım

### Checkpoint 1 — Butonlu taslak (üretim tarafı)

**Amaç:** Hem WF-01 hem WF-02 Telegram’a **Onayla / Reddet** göndersin; `callback_data` içinde satır `id` olsun.

1. Akış: `Code → Insert → Telegram` (Telegram Insert’ten **sonra**)
2. Telegram Text: Code’dan `telegram_message`
3. Inline butonlar:
   - Onayla → `approve:{{ $json.id }}`
   - Reddet → `reject:{{ $json.id }}`
4. Önce **WF-02**, sonra aynı buton ayarını **WF-01**’e kopyala

**Doğrulama:** İki hattan da butonlu mesaj geliyor mu?  
→ Evet ise söyle → **commit: `feat: telegram onay butonlari wf-01/02`**

---

### Checkpoint 2 — WF-04 iskeleti (callback + status)

**Amaç:** Butona basınca workflow çalışsın; Reddet/Onayla status yazsın.

1. Yeni workflow: `WF-04 Onay GorSel Yayin` (veya `WF-04 Telegram Onay`)
2. Telegram Trigger → **callback_query** → **Active**
3. Code: `approve:` / `reject:` + `content_id` parse
4. IF:
   - `rejected` → Data Table Update `status=rejected` → **bitir**
   - `approved` → Data Table Update `status=approved` → **devam** (sonraki node’lar)
5. (İsteğe bağlı) Answer callback / “Onaylandı” mesajı

**Doğrulama:** Onayla → `approved`, Reddet → `rejected`  
→ Evet ise söyle → **commit: `feat: wf-04 telegram callback status update`**

---

### Checkpoint 3 — Onay sonrası görsel

**Amaç:** Sadece **Onayla** dalında görsel üretilsin.

1. Approved dalında: Data Table **Get row** (`id` = content_id) — title, content, platform, visual_idea çek
2. Image node (OpenAI Images / seçtiğimiz sağlayıcı)
3. Prompt: `visual_idea` + platform
4. `image_url` veya binary’yi sakla; tabloya yaz (sütun yoksa ekle)

**Doğrulama:** Onayla → görsel oluşuyor; Reddet → görsel yok  
→ Evet ise söyle → **commit: `feat: onay sonrasi gorsel uretimi`**

---

### Checkpoint 4 — Yayın (bugün mümkün olduğu kadar)

**Amaç:** Platforma göre post.

1. IF `platform` = LinkedIn → LinkedIn node  
2. IF `platform` = Instagram → Instagram node  
3. Başarı → `status=published`  
4. Hata → WF-03 + `failed`

> Bugün API/credential hazır değilse: yayın node’larını **placeholder** bırakıp önce LinkedIn’i bitir; Instagram’ı ertesi güne bırak. Commit yine alınır (`feat: linkedin publish after approve` gibi).

**Doğrulama:** Onayla → görsel → ilgili platformda post (veya LinkedIn smoke test)  
→ Evet ise söyle → **commit**

---

## Bugün yapma (bilinçli ertele)

- Multi-agent, takvim, brand voice  
- İkinci “görsel onay” turu (tek Onayla yeterli)  
- execution_logs  

---

## Commit kuralı (senin isteğin)

Her checkpoint’te:

1. Sen: “sorunsuz çalışıyor”  
2. Ben: kısa kontrol listesi sorarım  
3. Export’ları güncelle  
4. Git commit (geri dönüş noktası)

---

## Şimdi hemen başla

**Sadece Checkpoint 1:**

1. WF-02’de Insert → Telegram; butonları ekle  
2. Bir kez çalıştır; Telegram’da Onayla/Reddet gör  
3. Aynı butonları WF-01’e uygula  
4. Yaz: “butonlar geldi” / takıldığın yer  

Sonra Checkpoint 2’ye (WF-04) geçeriz.
