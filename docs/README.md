# Proje Dokümantasyonu

Sosyal Medya İçerik Ajansı — n8n + AI ile LinkedIn/Instagram içerik üretimi.

## Ana dosyalar

| Dosya | İçerik |
|-------|--------|
| [proje-amaci.md](./proje-amaci.md) | Amaç, kapsam, hedefler |
| [yol-haritasi-onay-gorsel-yayin.md](./yol-haritasi-onay-gorsel-yayin.md) | **Sonraki aşama:** buton onayı + görsel + LinkedIn/Instagram yayın |
| [kullanilacak-teknolojiler.md](./kullanilacak-teknolojiler.md) | Docker, n8n, OpenAI, Telegram, RSS |
| [ogrenilecek-kavramlar.md](./ogrenilecek-kavramlar.md) | Öğrenilecek / öğrenilen checklist |
| [ogrenilen-bilgiler.md](./ogrenilen-bilgiler.md) | Pratik notlar |
| [planlanan-workflow-yapisi.md](./planlanan-workflow-yapisi.md) | WF-01 / 02 / 03 özeti |
| [akis-semasi.md](./akis-semasi.md) | Mermaid akış şemaları |
| [data-table-yapisi.md](./data-table-yapisi.md) | contents / errors / logs |
| [karsilasilan-problemler.md](./karsilasilan-problemler.md) | Takıldığımız sorunlar |
| [cozum-notlari.md](./cozum-notlari.md) | Nasıl çözdük |
| [ekran-goruntuleri/](./ekran-goruntuleri/) | Screenshot'lar |

## Çalışma notları (faz faz)

[`calisma-notlari/`](./calisma-notlari/) — kurulum adımları ve kararlar

## Proje planı

[`../proje-plani.md`](../proje-plani.md) — faz checklist (tamamlandı)

## Workflow export'ları (repo kökü)

| Dosya | Açıklama |
|--------|----------|
| `WF-01 Manuel İçerik Üretme.json` | Manuel konu → AI → tablo → Telegram |
| `WF-02 Kaynaktan İçerik Üretme.json` | RSS → duplicate → AI → tablo → Telegram |
| `WF-03 Error Handling.json` | Error Trigger → errors → Telegram HATA |

## Prompt'lar

| Dosya | Workflow |
|--------|----------|
| `prompts/manuel-icerik-prompt.md` | WF-01 |
| `prompts/kaynaktan-icerik-prompt.md` | WF-02 |
