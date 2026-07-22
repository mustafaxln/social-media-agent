# Telegram `/yeni` — Manuel giriş (kurulum notu)

**Durum:** ✅ Tamamlandı (Tem 2026)  
**Amaç:** n8n Edit Fields / Manual Trigger yerine Telegram DM ile konu üretmek (PM isteği)

## Neden?

PM: Manuel alanları n8n’de doldurmak yerine Telegram’dan girilsin; günlük n8n bağı kalksın.

## Mimari karar

| Seçenek | Sonuç |
|---------|--------|
| WF-01’e ayrı Telegram Trigger | ❌ Bot webhook çakışır |
| 2. bot | ❌ UX karmaşık; tercih edilmedi |
| Buton altı “yazı kutusu” | ❌ Telegram Bot API’de yok |
| **WF-04 hub + `/yeni` + Execute WF-01** | ✅ Seçilen |

`/yeni` **DM**; taslak **grup**. Grupta tetikleme denendi (privacy off, bot re-add, admin) — güvenilir olmadı.

## WF-01 değişiklikleri

1. **When Executed by Another Workflow**  
   - Input mode: Define using fields below  
   - Alanlar: `topic`, `platform`, `target_audience`, `tone` (String)  
2. Trigger → doğrudan AI Agent (Edit Fields bypass)  
3. AI User Message aynı: `$json.topic` vb.  
4. Telegram: grup Chat ID; Attribution OFF; Parse Mode yok  
5. WF-01 Active (çağrılabilsin)

## WF-04 değişiklikleri

1. Telegram Trigger Updates: `callback_query` **+** `message`  
2. **Giris Ayir** (Code) — `route`: `callback` | `yeni` | `ignore`  
3. Switch: `{{ $json.route }}` equals `callback` | `yeni`  
4. callback → mevcut Callback Parse (dokunulmadı)  
5. yeni → **Parse /yeni** → IF `ok` → **Execute Workflow** WF-01  

### Giris Ayir (özet mantık)

- `data` / callbackQuery.data → `approve|reject|publish|cancel:` ise `route=callback`  
- `text` `/yeni` ile başlıyorsa `route=yeni`  

### Parse /yeni

Satırları `platform:`, `konu:`, `hedef:`, `ton:` (veya EN eşleri) ile map eder; eksikte `ok:false` + hata metni.

## Kullanım

Şablon: [`../../templates/telegram/yeni-komut-sablonu.md`](../../templates/telegram/yeni-komut-sablonu.md)

```text
/yeni
platform: LinkedIn
konu: ...
hedef: ...
ton: Profesyonel ve öğretici
```

## Test sonucu

| Ortam | Sonuç |
|--------|--------|
| Bot DM | ✅ tetikler, içerik üretir |
| Grup | ❌ execution çoğu zaman yok → DM tercih |

## Takılıp çözülenler (bu faz)

| Sorun | Çözüm |
|--------|--------|
| Switch `callbackQuery.id` | Giris Ayir + `route` |
| `/yeni` tetiklenmiyor | Trigger’a `message` |
| parse entities | Attribution OFF |
| Grup | DM kabul edildi |
