from router import route

def test_weather():
    result = route("วันนี้อากาศเป็นยังไง")
    assert result["task"] == "weather"
    assert result["model"] == "typhoon"

def test_translate():
    result = route("แปลประโยคนี้เป็นอังกฤษ")
    assert result["task"] == "translate"
    assert result["model"] == "qwen"

def test_summarise():
    result = route("ช่วยสรุปข่าวนี้หน่อย")
    assert result["task"] == "summarise"
    assert result["model"] == "typhoon"

def test_fallback():
    result = route("สวัสดี")
    assert result["task"] == "chat"
    assert result["stage"] == "fallback"