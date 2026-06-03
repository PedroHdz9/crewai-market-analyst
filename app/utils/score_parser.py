import re


def extract_score(report, score_name):

    patterns = [

        rf"{re.escape(score_name)}.*?(\d+)/10",

        rf"{re.escape(score_name)}.*?(\d+)\s*sobre\s*10",

        rf"{re.escape(score_name)}.*?(\d+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            report,
            re.IGNORECASE | re.DOTALL
        )

        if match:

            try:
                return int(match.group(1))
            except:
                pass

    return None