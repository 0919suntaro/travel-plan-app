from pydantic import BaseModel, Field


class TouristSpot(BaseModel):
    name: str
    category: str = Field(description="例: 自然, 歴史・文化, グルメ, 絶景, 体験")
    description: str
    why_recommended: str
    best_time: str = Field(description="おすすめの季節・時間帯")


class TouristSpotList(BaseModel):
    spots: list[TouristSpot]


class DestinationSuggestion(BaseModel):
    destination: str
    region: str
    summary: str
    highlights: list[str]
    suggested_plan: str = Field(description="1〜2泊程度の簡単なプラン例")
    match_reason: str = Field(description="入力された雰囲気・希望とのマッチ理由")


class DestinationSuggestionList(BaseModel):
    suggestions: list[DestinationSuggestion]


class MountainSuggestion(BaseModel):
    name: str
    elevation_m: int
    region: str
    difficulty: str = Field(description="初級 / 中級 / 上級 のいずれか")
    standard_duration: str = Field(description="標準コースタイムの目安")
    highlights: str
    access: str = Field(description="登山口へのアクセス概要")
    notes: str = Field(description="装備や注意点など")


class MountainSuggestionList(BaseModel):
    mountains: list[MountainSuggestion]


class ItineraryDay(BaseModel):
    day: int
    theme: str
    morning: str
    afternoon: str
    evening: str
    notes: str = ""


class TripPlan(BaseModel):
    title: str
    overview: str
    days: list[ItineraryDay]
    budget_estimate: str
    tips: list[str]


class PackingCategory(BaseModel):
    category: str
    items: list[str]


class PackingListResponse(BaseModel):
    categories: list[PackingCategory]
    advice: str
