
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "W06_Progress_Presentation.pptx"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

NAVY = RGBColor(25, 45, 75)
GRAY = RGBColor(80, 90, 105)


def add_slide(title, points):
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(
        Inches(0.8), Inches(0.55),
        Inches(11.8), Inches(0.9)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.paragraphs[0].font.size = Pt(30)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = NAVY

    body_box = slide.shapes.add_textbox(
        Inches(0.9), Inches(1.7),
        Inches(11.5), Inches(5.1)
    )
    body_frame = body_box.text_frame
    body_frame.word_wrap = True

    for index, point in enumerate(points):
        paragraph = (
            body_frame.paragraphs[0]
            if index == 0
            else body_frame.add_paragraph()
        )
        paragraph.text = "• " + point
        paragraph.font.size = Pt(21)
        paragraph.font.color.rgb = GRAY
        paragraph.space_after = Pt(18)

    footer = slide.shapes.add_textbox(
        Inches(0.8), Inches(7.0),
        Inches(11.5), Inches(0.3)
    )
    footer.text_frame.text = (
        "CISC 699 | A2 Research | Week 6 Progress Review"
    )
    footer.text_frame.paragraphs[0].font.size = Pt(11)


add_slide("A2 Research — Week 6 Progress Review", [
    "Natural-Language Edge Semantics and Deterministic Agent Execution",
    "Harrisburg University | CISC 699 Capstone II",
    "Progress presentation draft — December 7–13, 2026",
])

add_slide("Research Objective", [
    "Interpret natural-language workflow edge conditions.",
    "Convert interpretations into structured semantic contracts.",
    "Validate contracts before deterministic routing.",
    "Record routing decisions for auditability and reproducibility.",
])

add_slide("Prototype Architecture", [
    "Natural-language edge descriptions",
    "Ollama structured interpretation",
    "Semantic contract construction and validation",
    "Deterministic predicate evaluation and graph enforcement",
    "Execution trace creation and JSON persistence",
])

add_slide("Implemented Prototype", [
    "Three-node workflow: Check Tests, Deploy Code, Fix Code.",
    "Two natural-language edge conditions.",
    "Boolean workflow field: tests_passed.",
    "Routing statuses include ROUTED, NO_MATCH, and AMBIGUOUS.",
    "Graph permissions and execution tracing are implemented.",
])

add_slide("Verified Pilot Evidence", [
    "Ollama contract generation and validation: PASS.",
    "Passing-test and failing-test routing: PASS.",
    "Repeated deterministic routing: PASS.",
    "Automatic execution trace saving: PASS.",
    "Unique trace identifiers: PASS.",
    "Evidence: test_ollama_workflow_integration.py, run November 13.",
])

add_slide("Baseline and Scenario Readiness", [
    "Original direct-LLM routing baseline implemented.",
    "Prompt-controlled direct-LLM baseline implemented.",
    "Structured-contract routing comparison implemented.",
    "Ten independent paraphrases reviewed: five pass, five fail.",
    "Full controlled comparison not rerun for this checkpoint.",
])

add_slide("Limitations and Research Risks", [
    "Current pilot is restricted to one Boolean workflow condition.",
    "Ten paraphrases do not establish broad language understanding.",
    "Direct and structured approaches have different LLM-call costs.",
    "Prompt differences may affect comparisons.",
    "Formal Week 9 evaluation results are not claimed here.",
])

add_slide("Next Steps and Feedback", [
    "Demonstrate the existing prototype and trace behavior.",
    "Present scenario and evaluation-oracle design.",
    "Collect instructor feedback and record action items.",
    "Address verified integration defects during Week 7.",
    "Conduct formal controlled evaluation in Week 9.",
])

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUTPUT)

print(f"Presentation created: {OUTPUT}")
print(f"Slides: {len(prs.slides)}")
