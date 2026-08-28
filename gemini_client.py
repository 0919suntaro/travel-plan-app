from google import genai
from google.genai import types
from pydantic import BaseModel

import config

SYSTEM_INSTRUCTION = (
    "あなたは日本語で回答する、旅行・登山に精通したプロのプランナー兼ガイドです。"
    "実在する場所・山を優先して具体的かつ実用的に提案してください。"
    "情報に確信が持てない場合は、一般的に知られている範囲で無理のない推定を行い、"
    "断定的すぎる表現は避けてください。"
)

_client: genai.Client | None = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        if not config.GEMINI_API_KEY:
            raise RuntimeError(
                "GEMINI_API_KEY が設定されていません。.env に設定するか、"
                "サイドバーから入力してください。"
            )
        _client = genai.Client(api_key=config.GEMINI_API_KEY)
    return _client


def reset_client() -> None:
    """Force the client to be rebuilt (e.g. after the API key changes)."""
    global _client
    _client = None


def generate_structured(prompt: str, schema: type[BaseModel]) -> BaseModel:
    client = _get_client()
    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=schema,
            temperature=0.8,
        ),
    )
    parsed = response.parsed
    if parsed is None:
        raise RuntimeError("Geminiからの応答を解析できませんでした。もう一度お試しください。")
    return parsed
