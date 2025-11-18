# test_keyword_check.py
from keyword_check import check_keywords

def test_all_keywords_present(capsys):
    text = "Power Platform, Power Apps, Power Automate, Power BI, Dataverse, Dynamics 365, SharePoint, Microsoft 365, Azure DevOps, GitHub"
    check_keywords(text)
    captured = capsys.readouterr()
    assert "All required keywords are present" in captured.out
