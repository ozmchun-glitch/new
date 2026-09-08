"""stat.uz saytidan oxirgi inflyatsiya yangiligining sarlavhasini topadi."""

import asyncio
import os

from browser_use import Agent, BrowserProfile
from browser_use.llm import BaseChatModel, ChatBrowserUse, ChatOpenAI

TASK = (
    "stat.uz saytiga kir, oxirgi inflyatsiya bo'yicha yangilikni top "
    "va sarlavhasini qaytar"
)


def build_llm() -> BaseChatModel:
    """Mavjud kalitga qarab LLM tanlaydi."""
    if os.getenv("BROWSER_USE_API_KEY"):
        return ChatBrowserUse(model=os.getenv("BROWSER_USE_MODEL", "bu-2-0"))
    if os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o"))
    raise SystemExit(
        "Kalit topilmadi. .env faylga BROWSER_USE_API_KEY yoki "
        "OPENAI_API_KEY qo'shing."
    )


def build_profile() -> BrowserProfile:
    """Konteyner/CI muhitida ham ishlaydigan brauzer profili."""
    args = ["--disable-dev-shm-usage"]
    if os.geteuid() == 0:
        # root ostida Chrome sandbox bilan ishga tushmaydi
        args.append("--no-sandbox")

    return BrowserProfile(
        executable_path=os.getenv("CHROME_PATH") or None,
        headless=os.getenv("HEADLESS", "true").lower() != "false",
        args=args,
    )


async def main() -> None:
    agent = Agent(task=TASK, llm=build_llm(), browser_profile=build_profile())
    history = await agent.run(max_steps=15)

    result = history.final_result()
    if result:
        print(result)
    else:
        print("Natija topilmadi. Xatolar:", history.errors())


if __name__ == "__main__":
    asyncio.run(main())
