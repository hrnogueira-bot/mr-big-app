# Mr Big App — como publicar

Site: https://hrnogueira-bot.github.io/mr-big-app/ (GitHub Pages, ramo `main`, raiz).

- Fonte da app: `fonte/app.src.html` (app inteira num ficheiro; marcadores `__EMBLEM__`, `__LOGO__`, `__PLAN__`, `__PHOTOS__`).
- Planta: `fonte/planta.json`. Fotos: `fonte/fotos.json` (base64). Logos: `fonte/emblema.jpg`, `fonte/logo.jpg`.
- `fonte/build.py` gera `index.html` na raiz e muda a versão da cache em `sw.js`.

Para publicar: editar ficheiros em `fonte/`, fazer commit e push para `main`.
A GitHub Action `.github/workflows/build.yml` corre o build e publica sozinha (~1–2 min).
Não editar `index.html` à mão: é gerado.
