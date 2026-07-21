# Telegram Hata Mesajı

WF-03 Error Handling — Code node `Hata Mesaji` üretir; Telegram Text:

```
{{ $('Hata Mesaji').item.json.telegram_message }}
```

## Code özeti

Error Trigger'dan `workflow.name`, `execution.id`, `execution.lastNodeExecuted`, `execution.error.message` okunur; boşsa tüm payload `error_message` olarak yazılır.

Şablon içeriği:

```
Sosyal Medya Agent — HATA

Workflow: ...
Execution: ...
Node: ...

Hata:
...

Zaman: ...
```

## Not

- Aynı Telegram grubuna gider; başlıkta `HATA` ile taslaklardan ayrılır.
- Append n8n Attribution kapalı tut.
