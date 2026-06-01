"""V39 — v34 com prompt permissivo: LLM so rejeita se MUITO certo que e outra doenca."""
import sys
sys.path.insert(0, "src")
import v34_ollama_classifier as v34

v34.PROMPT = """You are reviewing ICD-10-CM codes for inclusion in a clinical query.

CONDITION: {condition}

For each ICD-10-CM code below, label:
- KEEP: the code COULD plausibly represent this condition or any of its variants, manifestations, complications, anatomic sites, severity grades, or related congenital/neonatal/obstetric forms. When in doubt, KEEP.
- IRRELEVANT: ONLY mark IRRELEVANT if you are 100% certain the code represents a clearly different disease (e.g., asthma is NOT pneumonia, ulcer is NOT epistaxis).

Default: KEEP. Be extremely permissive.

CODES:
{candidates}

Output ONLY a JSON array: [{{"code":"X","label":"KEEP"}},...]. No prose."""

v34.OLLAMA_MODEL = "qwen2.5:7b"

# substitui o write target
original_main = v34.main


def main_wrapper():
    original_write = v34.write_submission
    def write_v39(rows, path):
        original_write(rows, "submissions/v39_ollama_permissive.csv")
    v34.write_submission = write_v39
    original_main()


if __name__ == "__main__":
    main_wrapper()
