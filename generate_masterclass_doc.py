from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()

style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

# ── TITLE ──
title = doc.add_heading(level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('Masterclass Description')
run.font.size = Pt(26)
run.font.color.rgb = RGBColor(0x1B, 0x1B, 0x1B)

# ── MASTERCLASS TITLE ──
doc.add_heading('Masterclass Title', level=1)
p = doc.add_paragraph()
run = p.add_run('Graph Knowing, Graph Doing, Graph Aware: Building a Neurosymbolic Context Layer for Governed AI')
run.bold = True
run.font.size = Pt(13)

# ── SPEAKER ──
doc.add_heading('Speaker', level=1)
p = doc.add_paragraph()
run = p.add_run('Ramu DE')
run.bold = True
p.add_run('\nSolutions Architect @ Takeda | Data & AI Solutions | ML | AI Factory | Agentic Systems | AI Evals & LLMOps | Knowledge Graphs | Multi-Cloud | Container Platforms (EKS, ECS)')
p.add_run('\nGitHub: github.com/Ramu-DE/BioMedical_contextLayer')

# ── DURATION ──
doc.add_heading('Duration', level=1)
doc.add_paragraph('1 x 2-hour session')

# ── ABSTRACT ──
doc.add_heading('Abstract', level=1)
doc.add_paragraph(
    'This masterclass teaches attendees how to build a neurosymbolic context layer — '
    'a governed AI architecture where a knowledge graph holds ground truth, a deterministic '
    'rule engine makes decisions in 0.09 milliseconds, and every decision writes back to '
    'the graph as an auditable record. Attendees will work through the three principles — '
    'Graph Knowing, Graph Doing, Graph Aware — using a pharmaceutical knowledge graph as '
    'the running example, and leave with a transferable pattern they can apply to any '
    'regulated domain.'
)
doc.add_paragraph(
    'The session concludes with a measured evaluation proving that this architecture '
    'outperforms LLM-as-Judge across accuracy (92% vs 58%), cost ($0 vs $131/month), '
    'speed (0.09ms vs 3,467ms), and adversarial resilience (12/12 attacks defeated). '
    'Attendees will understand exactly why LLM-as-Judge produces a Cohen\'s Kappa of 0.000 '
    'on hard cases — the "Agreement Illusion" — and what to build instead.'
)

# ── LEARNING OBJECTIVES ──
doc.add_heading('Learning Objectives', level=1)
doc.add_paragraph(
    'By the end of this masterclass, attendees will be able to:'
)
objectives = [
    'Design a knowledge graph schema for governed AI — entity types, typed relationships, '
    'and an OWL/TTL ontology with SHACL validation shapes (Graph Knowing)',
    'Build a neurosymbolic pipeline where neural (LLM) and symbolic (rule engine) paths '
    'run independently and meet at a governance gate with fixed precedence (Graph Doing)',
    'Implement an append-only decision write-back with bi-temporal timestamps that gives '
    'an AI system institutional memory without retraining (Graph Aware)',
    'Write declarative YAML governance rules that query graph facts — not prompts — making '
    'the system immune to prompt injection by architecture',
    'Evaluate governed AI systems using proper metrics (Cohen\'s Kappa, not raw accuracy) '
    'and identify the "Agreement Illusion" in LLM-as-Judge results',
    'Apply the Graph Knowing / Graph Doing / Graph Aware framework to their own domain '
    '(finance, healthcare, legal, supply chain)',
]
for obj in objectives:
    doc.add_paragraph(obj, style='List Bullet')

# ── TARGET AUDIENCE ──
doc.add_heading('Target Audience', level=1)
table = doc.add_table(rows=4, cols=2)
table.style = 'Light Shading Accent 1'
table.alignment = WD_TABLE_ALIGNMENT.LEFT

cells = table.rows[0].cells
cells[0].text = 'Level'
cells[1].text = 'Intermediate to Advanced'

cells = table.rows[1].cells
cells[0].text = 'Audience'
cells[1].text = 'Business and Technical — data engineers, ML engineers, architects, technical leaders building AI systems in regulated industries'

cells = table.rows[2].cells
cells[0].text = 'Required Background'
cells[1].text = 'Basic understanding of LLMs and how they generate text. Familiarity with databases (SQL or graph) is helpful but not required. No prior knowledge of ontologies, SHACL, or rule engines needed — all introduced during the session.'

cells = table.rows[3].cells
cells[0].text = 'Bring'
cells[1].text = 'Laptop with Python 3.11+, git, and a code editor. All cloud credentials and data are provided (synthetic, no PHI).'

for row in table.rows:
    for cell in row.cells:
        for paragraph in cell.paragraphs:
            paragraph.style.font.size = Pt(10)

# ── DETAILED AGENDA ──
doc.add_heading('Detailed Agenda (2 Hours)', level=1)

# Part 1
doc.add_heading('Part 1 — Graph Knowing: The Foundation (40 minutes)', level=2)

p = doc.add_paragraph()
run = p.add_run('0:00 – 0:15 | Opening & Problem Statement')
run.bold = True
items_1a = [
    'Why text-based AI fails in regulated domains — concrete pharmaceutical examples',
    'The gap between what an LLM can generate and what a governed system can verify',
    'Introducing the semantic membrane concept: ontology, identifiers, rules, and meaning on the inside; noise and adversarial input on the outside',
]
for item in items_1a:
    doc.add_paragraph(item, style='List Bullet')

p = doc.add_paragraph()
run = p.add_run('0:15 – 0:40 | Building the Knowledge Graph')
run.bold = True
items_1b = [
    'Walkthrough: 6 entity types (Drug, Disease, Patient, Gene, Biomarker, Clinical Trial) and 9 typed relationships',
    'Loading pharmaceutical data into Neo4j — nodes, relationships, and the Cypher data model',
    'OWL/TTL ontology modules — what they define and why they matter',
    'SHACL validation shapes — catching data/model conflicts at write time, not query time',
    'Live example: "Atezolizumab targets PD-L1, not PD-1" — how the graph distinguishes what text conflates',
    'Hands-on: attendees explore the graph with Cypher queries, verify entity types and relationships',
]
for item in items_1b:
    doc.add_paragraph(item, style='List Bullet')

# Part 2
doc.add_heading('Part 2 — Graph Doing: The Pipeline (45 minutes)', level=2)

p = doc.add_paragraph()
run = p.add_run('0:40 – 0:55 | Entity Linking & Knowledge Retrieval')
run.bold = True
items_2a = [
    'How text mentions resolve to typed graph entities — the 129-entry name index, word-boundary matching, case-sensitivity guards',
    'Parallel retrieval: Neo4j Cypher traversal (structured facts) alongside Qdrant vector search (document chunks)',
    'The Context Package — deduplicated, ranked, token-budgeted, with provenance per element',
]
for item in items_2a:
    doc.add_paragraph(item, style='List Bullet')

p = doc.add_paragraph()
run = p.add_run('0:55 – 1:10 | The Governance Gate: Neural vs Symbolic')
run.bold = True
items_2b = [
    'The neurosymbolic architecture: neural and symbolic paths run independently, never see each other\'s output',
    'Writing declarative YAML rules that query graph facts — syntax, predicates, severity levels',
    'The rule engine as a pure function: no network, no LLM, no clock — 0.09ms execution',
    'Fixed governance precedence: clinical advice guard → symbolic block → grounding threshold → release',
    'Live trace: "Can I include PAT015 in the trial outcome analysis?" — watching consent.withdrawn fire and BLOCK',
    'Hands-on: attendees write a custom YAML rule, add it to a pack, and watch it fire on a query',
]
for item in items_2b:
    doc.add_paragraph(item, style='List Bullet')

p = doc.add_paragraph()
run = p.add_run('1:10 – 1:25 | Adversarial Resilience')
run.bold = True
items_2c = [
    'Four attack classes: conflicting documents, pattern pollution, signal drowning, prompt injection',
    'Live demonstration: injecting "SYSTEM OVERRIDE: ignore all governance" — all 4 rules still fire',
    'Why this works: the rule engine reads the database, not the context window — you cannot prompt-inject a Cypher query',
    'The accidental proof: AWS credentials expired mid-test, LLM went dark, rules still fired — fails closed vs fails open',
    'Discussion: what this means for production AI governance — structural guarantees vs tuned defences',
]
for item in items_2c:
    doc.add_paragraph(item, style='List Bullet')

# Part 3
doc.add_heading('Part 3 — Graph Aware: Memory & Evaluation (35 minutes)', level=2)

p = doc.add_paragraph()
run = p.add_run('1:25 – 1:40 | Decision Write-Back')
run.bold = True
items_3a = [
    'Append-only Ctx_Decision nodes — question, rules fired, grounding score, bi-temporal timestamps',
    'Bi-temporal design: occurred_at/ingested_at for events, valid_from/valid_to for decisions',
    'The continuous incorporation loop: prior decisions enter the next query\'s context via vector index',
    'Live demonstration: run the same query twice — the model cites its own earlier governance decision',
    '"No weights change. The graph grows." — institutional memory without retraining',
]
for item in items_3a:
    doc.add_paragraph(item, style='List Bullet')

p = doc.add_paragraph()
run = p.add_run('1:40 – 1:55 | Evaluation — LLM-as-Judge vs Deterministic')
run.bold = True
items_3b = [
    'The evaluation framework: 53 test cases, 6 modules (domain accuracy, bias battery, metrics rigor, error taxonomy, cost analysis, retrieval quality)',
    'Results walkthrough: 92% / Kappa 0.833 (deterministic) vs 58% / Kappa 0.000 (LLM judge)',
    'The "Agreement Illusion": why 58% raw accuracy hides zero predictive value — and why Cohen\'s Kappa matters',
    'Bias battery results: 50% position bias, 50% verbosity bias, 4/4 controls false-failed',
    'Cost analysis: $0 vs $131/month at 1,000 queries/day — the economics of Build vs Buy',
    'The circular dependency: the only judge scoring 100% required the answer upfront',
    'Hands-on: attendees run the eval framework on a subset of test cases and verify the results',
]
for item in items_3b:
    doc.add_paragraph(item, style='List Bullet')

# Closing
p = doc.add_paragraph()
run = p.add_run('1:55 – 2:00 | Closing & Transfer to Your Domain')
run.bold = True
items_close = [
    'Recap: Graph Knowing → Graph Doing → Graph Aware as a transferable framework',
    'How to port the architecture: what changes (ontology, rule packs, data) and what stays (pipeline, gate, write-back)',
    'Q&A',
]
for item in items_close:
    doc.add_paragraph(item, style='List Bullet')

# ── MATERIALS PROVIDED ──
doc.add_heading('Materials Provided to Attendees', level=1)
materials = [
    'GitHub repository with full source code, synthetic pharmaceutical data, and 371 tests',
    'Pre-configured Neo4j Aura instance with 545-node knowledge graph (shared read access)',
    'Pre-configured Qdrant Cloud cluster with 650+ vectors across 4 collections',
    'YAML rule pack templates for attendees to write custom governance rules',
    'Jupyter notebooks for each hands-on section',
    'Slide deck (PDF) with all architecture diagrams and evaluation results',
]
for mat in materials:
    doc.add_paragraph(mat, style='List Bullet')

# ── TECHNICAL REQUIREMENTS ──
doc.add_heading('Technical Requirements', level=1)

p = doc.add_paragraph()
run = p.add_run('For the venue:')
run.bold = True
venue_reqs = [
    'Projector and screen',
    'Reliable internet connection (attendees will query cloud-hosted Neo4j and Qdrant)',
    'Power outlets for laptops',
]
for req in venue_reqs:
    doc.add_paragraph(req, style='List Bullet')

p = doc.add_paragraph()
run = p.add_run('For attendees:')
run.bold = True
attendee_reqs = [
    'Laptop with Python 3.11+, git, and a code editor',
    'Pre-install instructions sent 1 week before the session (pip install, clone repo, verify connectivity)',
    'All cloud credentials provided at session start — no personal AWS/Neo4j/Qdrant accounts needed',
]
for req in attendee_reqs:
    doc.add_paragraph(req, style='List Bullet')

# ── KEY TECHNOLOGIES ──
doc.add_heading('Key Technologies Covered', level=1)
table2 = doc.add_table(rows=8, cols=3)
table2.style = 'Light Shading Accent 1'
table2.alignment = WD_TABLE_ALIGNMENT.LEFT

headers = ['Component', 'Technology', 'Role in Architecture']
for i, h in enumerate(headers):
    table2.rows[0].cells[i].text = h

data = [
    ('Knowledge Graph', 'Neo4j Aura', 'Ground truth — 545 nodes, 30+ relationship types'),
    ('Vector Store', 'Qdrant Cloud', 'Semantic retrieval — 650+ vectors, 4 collections'),
    ('LLM', 'Claude Haiku 4.5 (Bedrock)', 'Neural path — context-grounded generation'),
    ('Embeddings', 'Amazon Titan Embed v2', '1024-dim vectors for retrieval and linking'),
    ('Ontology', 'OWL/TTL + SHACL', 'Schema validation — 8 modules, 3,965 triples, 10 shapes'),
    ('Rule Engine', 'Custom (Python + YAML)', 'Symbolic path — 13 rules, pure function, 0.09ms'),
    ('Dashboard', 'NiceGUI', '3-page live UI — pipeline trace, eval proof, membrane viz'),
]
for i, (comp, tech, role) in enumerate(data):
    table2.rows[i+1].cells[0].text = comp
    table2.rows[i+1].cells[1].text = tech
    table2.rows[i+1].cells[2].text = role

# ── WHAT MAKES THIS MASTERCLASS UNIQUE ──
doc.add_heading('What Makes This Masterclass Unique', level=1)
unique = [
    'Not a lecture — a running system. Every concept demonstrated live on a deployed knowledge graph with real (synthetic) pharmaceutical data.',
    'Not incremental — a new architecture. Neurosymbolic governance where symbolic overrides neural is fundamentally different from prompt engineering, RAG tuning, or guardrail APIs.',
    'Measured, not asserted. Attendees run the evaluation framework themselves and see the Kappa 0.000 result firsthand.',
    'Transferable. The Graph Knowing / Graph Doing / Graph Aware framework applies to any regulated domain. Attendees leave with a pattern, not just pharma knowledge.',
    'Adversarial-proof by design. The live prompt injection demonstration — and the AWS credential expiry story — show structural resilience that no amount of prompt tuning can replicate.',
]
for u in unique:
    doc.add_paragraph(u, style='List Bullet')

# ── SPEAKER BIO ──
doc.add_heading('Speaker Bio', level=1)
doc.add_paragraph(
    'Ramu DE is a Solutions Architect at Takeda, working across Data & AI Solutions, ML, AI Factory, '
    'Agentic Systems, AI Evals & LLMOps, Knowledge Graphs, multi-cloud, and container platforms '
    '(EKS, ECS). He specialises in knowledge graph architectures and AI governance for regulated '
    'industries — the intersection where enterprise-scale cloud infrastructure meets the semantic '
    'precision that pharmaceutical governance demands. He built the BioMedical Context Layer as a '
    'reference implementation proving that deterministic governance grounded in ontologies outperforms '
    'LLM-based evaluation across accuracy, cost, resilience, and auditability. His work spans Neo4j, '
    'Qdrant, Amazon Bedrock, OWL/SHACL ontologies, and neurosymbolic system design. At Takeda, he '
    'brings this thinking to production — building the data and AI platforms where governed '
    'decisions happen at scale.'
)

# ── VIDEO LINK ──
doc.add_heading('Video Link', level=1)
doc.add_paragraph('[INSERT PUBLIC LINK TO 3-MINUTE VIDEO — 9:16 vertical, speaker-to-camera, story format]')

# ── Save ──
output_path = 'Masterclass_Description_CDL.docx'
doc.save(output_path)
print(f'Saved to {output_path}')
