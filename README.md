# stat.uz inflyatsiya yangiligi agenti

[browser-use](https://github.com/browser-use/browser-use) yordamida `stat.uz`
saytidan oxirgi inflyatsiya bo'yicha yangilikning sarlavhasini topadi.

## O'rnatish

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Chromium kerak (bir marta):

```bash
playwright install chromium
```

Yoki tizimda mavjud brauzerni ko'rsating: `CHROME_PATH=/usr/bin/chromium`.

## Sozlash

`.env.example` nusxasini `.env` qilib oling va OpenAI kalitini kiriting:

```bash
cp .env.example .env
```

## Ishga tushirish

```bash
export OPENAI_API_KEY=sk-...
python main.py
```

Brauzerni ko'rinadigan rejimda kuzatish uchun: `HEADLESS=false python main.py`.

## Muhit talablari

Skript ishlashi uchun tarmoqdan quyidagilarga kirish ochiq bo'lishi kerak:

- `stat.uz` — agent ochadigan sayt
- `api.openai.com` — LLM chaqiruvlari

Cheklangan (egress-filtrlangan) muhitlarda bu hostlar bloklansa, agent
navigatsiyada `site unavailable` xatosi bilan to'xtaydi.
