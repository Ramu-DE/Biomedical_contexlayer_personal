# Oxford Abstracts — Compact Outline (for pasting into form)

Character counts provided per section. Total outline below: ~3,400 characters.

---

## PASTE THIS:

**The Problem**

When you ask an LLM a question about drugs, patients, or clinical trials, the LLM reads text and generates an answer. But text can be wrong. Text can contradict itself. Text can be injected. And the LLM has no way to tell the difference. In regulated industries — pharmaceuticals, finance, healthcare — a wrong decision about patient consent or drug safety is not a poor user experience; it is a compliance failure with real consequences.

The facts that govern these decisions live in structured graphs — consent status, drug targets, trial phases, adverse event severity. A language model reading retrieved text cannot verify whether an action is permitted when the ground truth is a typed relationship in a database, not a sentence in a document.

**Why This Matters to Attendees and the World**

Every organisation deploying AI in a governed domain needs a layer between the model and the decision — a layer grounded in verified facts, not generated text. This is not a nice-to-have; it is a regulatory requirement in pharma and an emerging expectation across finance, healthcare, legal, and supply chain.

**How We Addressed It — The BioMedical Context Layer**

We built a running neurosymbolic system — not a framework or proposal — structured around three principles:

Graph Knowing. The graph holds ground truth. A pharmaceutical knowledge graph in Neo4j — 545 nodes covering drugs, patients, clinical trials, adverse events, genes, and biomarkers — connected by 30 typed relationships. An OWL/TTL ontology with SHACL validation shapes defines what is structurally true. Atezolizumab targets PD-L1, not PD-1. PAT015 consent is Withdrawn, not Active. Graph facts — validated, typed, deterministic. The knowledge graph is the semantic membrane: structure and meaning on the inside; noise and adversarial input on the outside.

Graph Doing. The graph makes decisions. A 4-stage pipeline routes every query through parallel neural and symbolic paths that never see each other's output. The LLM responds in ~9 seconds. The rule engine queries Neo4j and returns its verdict in 0.09 milliseconds. 13 declarative YAML rules enforce fixed governance precedence: symbolic overrides neural. The rule engine reads the graph — it never reads the prompt. Governance held 12/12 across four attack classes including prompt injection. When AWS credentials expired mid-test and the LLM went dark, all rules still fired. Fails closed, not open.

Graph Aware. The graph remembers what it decided. Every response writes an append-only decision node back to Neo4j — question, rules fired, grounding score, bi-temporal timestamps. The graph grows. No model weights change. Every decision is auditable.

**How We Evaluated It — LLM-as-Judge vs Deterministic**

53 pharmaceutical test cases, 6 modules. Deterministic context layer: 92% accuracy, Cohen's Kappa 0.833. LLM judge without ground truth: 58% accuracy, Kappa 0.000 — zero predictive value. 50% position bias, 50% verbosity bias, 4/4 controls false-failed. Cost: $0 vs $131/month. Speed: 0.09ms vs 3,467ms.

**Impact**

Open-source, 371 tests, live 3-page dashboard, fully synthetic data. Adversarial-proof by architecture, not tuning. Domain-portable — swap the ontology and rule packs for finance, healthcare, or legal.

**Target Audience**

Business and technical. Intermediate to advanced. Required background: basic understanding of LLMs and why evaluation matters. No graph database or ontology experience needed — introduced through pharmaceutical domain examples.

**What Attendees Will Take Away**

1. A transferable framework — Graph Knowing, Graph Doing, Graph Aware — for governed AI in any regulated domain
2. A running neurosymbolic architecture they can clone, not a diagram
3. Measured proof that LLM-as-Judge has zero predictive value on hard cases (the "Agreement Illusion")
4. The economics of Build vs Buy — ontology, rules, and graph as an appreciating asset vs recurring API costs
5. Adversarial resilience as a structural property — you cannot prompt-inject a database query

**Video Link:** [INSERT LINK]

---

## IF STILL OVER LIMIT — CUT IN THIS ORDER:

1. Remove "Atezolizumab targets PD-L1, not PD-1. PAT015 consent is Withdrawn, not Active." from Graph Knowing (saves ~100 chars)
2. Shorten "Why This Matters" to: "Every organisation deploying AI in a governed domain needs a layer between the model and the decision — grounded in verified facts, not generated text. A regulatory requirement in pharma, an emerging expectation across finance, healthcare, legal, and supply chain." (saves ~80 chars)
3. Compress Impact to: "Open-source, 371 tests, live dashboard, synthetic data. Domain-portable — swap ontology and rules for any regulated domain." (saves ~60 chars)
4. Reduce takeaways to 3 (keep 1, 3, 5) (saves ~200 chars)

## IF YOU HAVE MORE ROOM — ADD IN THIS ORDER:

1. Under Evaluation: "The only judge variant scoring 100% required the correct answer upfront — a circular dependency that eliminates the need for a judge."
2. Under Graph Doing: "A user asks: Can I include PAT015 in the trial outcome analysis? patient_consent.yaml fires — consent Withdrawn, BLOCK."
3. Under Impact: "A Palantir Foundry-style ontology engine (233 typed objects, 449 links) layers over results for structured analysis."
