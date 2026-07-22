# Ekran Görüntüleri

## Önemli not

Bu ortamdan **local n8n** (`localhost:5678`) arayüzüne girilip otomatik screenshot alınamaz.  
Aşağıdaki mevcut dosyalar erken dönem (Faz 2–3) testleridir. Final sistem için **çekim listesini** sen tamamlamalısın.

## Mevcut dosyalar

| Dosya | Dönem | Açıklama |
|-------|--------|----------|
| `Screenshot 2026-07-06 at 13.21.34.png` | Tem 2026 başı | n8n / WF erken test |
| `Screenshot 2026-07-06 at 13.21.50.png` | Tem 2026 başı | Node / arayüz |
| `Screenshot 2026-07-06 at 13.21.59.png` | Tem 2026 başı | Workflow / çıktı |
| `Screenshot 2026-07-06 at 13.23.51.png` | Tem 2026 başı | Test ekranı |

## Çekim listesi (final — PM / teslim için)

Dosyaları bu klasöre koy; tabloyu güncelle.

### Workflow canvas
- [ ] `wf-01-canvas.png` — WF-01 tam akış
- [ ] `wf-02-canvas.png` — RSS → Duplicate → Limit → … → Telegram
- [ ] `wf-03-canvas.png` — Error Trigger → Code → Insert → Telegram
- [ ] `wf-04-canvas.png` — Switch (approve/reject/publish/cancel) + Image + Cloudinary + Buffer

### Telegram
- [ ] `telegram-taslak-buton.png` — Onayla / Reddet
- [ ] `telegram-final-foto.png` — Final foto + Yayınla / İptal
- [ ] `telegram-hata.png` — WF-03 HATA mesajı

### Data Table
- [ ] `datatable-waiting.png` — waiting_approval satırı
- [ ] `datatable-published.png` — published + image_url dolu
- [ ] `datatable-errors.png` — social_media_errors örneği

### Yayın
- [ ] `linkedin-post.png` veya Buffer kuyruk ekranı
- [ ] `instagram-post.png` veya Buffer

### n8n
- [ ] `n8n-executions-success.png` — WF-04 success execution
- [ ] `n8n-error-workflow-settings.png` — Error Workflow = WF-03

## Nasıl çekilir (Mac)

1. n8n’i aç → ilgili workflow  
2. `Cmd+Shift+4` (alan seç) veya `Cmd+Shift+3`  
3. Dosyayı `docs/ekran-goruntuleri/` içine taşı  
4. Anlamlı ad ver (yukarıdaki liste)  
5. Bu README tablosuna satır ekle  

## İsimlendirme önerisi

`YYYY-MM-DD-kisa-aciklama.png`
