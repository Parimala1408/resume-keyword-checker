from keyword_check import check_keywords

def test_all_keywords_present(capsys):
    required = ["Power Platform", "Power Apps"]
    text = "Working on Power Platform using Power Apps"
    check_keywords(text, required)
    captured = capsys.readouterr()
    assert "All required keywords are present" in captured.out
