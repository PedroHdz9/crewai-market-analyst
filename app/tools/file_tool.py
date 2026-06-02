from pathlib import Path

class FileTool:

    @staticmethod
    def save_report(content, filename):
        path = Path("reports") / filename

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)