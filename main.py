"""stat.uz saytidan oxirgi inflyatsiya yangiligining sarlavhasini topadi."""

import asyncio
import os

from browser_use import Agent, BrowserProfile, ChatOpenAI

TASK = (
    "stat.uz saytiga kir, oxirgi inflyatsiya bo'yicha yangilikni top "
    "va sarlavhasini qaytar"
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
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY o'rnatilmagan. .env faylga qo'shing.")

    agent = Agent(
        task=TASK,
        llm=ChatOpenAI(model="gpt-4o"),
        browser_profile=build_profile(),
    )
    history = await agent.run(max_steps=15)

    result = history.final_result()
    if result:
        print(result)
    else:
        print("Natija topilmadi. Xatolar:", history.errors())


if __name__ == "__main__":
    asyncio.run(main())
