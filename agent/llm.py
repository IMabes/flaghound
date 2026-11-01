"""Claude modeline mesaj gönderip cevap döndüren ince katman."""

from anthropic import Anthropic
from agent.config import settings

#Anahtarı config'ten alır
client = Anthropic(api_key=settings.llm_api_key)


def ask(prompt: str) -> str:
    """Modele tek bir mesaj gönderir ve metin cevabını döndürür.""" 
    response = client.messages.create(
        model = settings.llm_model,
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.content[0].text
