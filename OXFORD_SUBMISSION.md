# Oxford Abstracts — CDL London Talk Submission

---

## TITLE

**Graph Knowing, Graph Doing, Graph Aware: A Neurosymbolic Context Layer for Pharmaceutical AI Governance**

---

## OUTLINE (paste into submission form)

### The Problem

When you ask an LLM a question about drugs, patients, or clinical trials, the LLM reads text and generates an answer. But text can be wrong. Text can contradict itself. Text can be injected. And the LLM has no way to tell the difference. In regulated industries — pharmaceuticals, finance, healthcare — a wrong decision about patient consent or drug safety is not a poor user experience; it is a compliance failure with real consequences.

The facts that govern these decisions live in structured graphs — consent status, drug targets, trial phases, adverse event severity. A language model reading retrieved text cannot verify whether an action is permitted when the ground truth is a typed relationship in a database, not a sentence in a document.

### Why This Matters to Attendees and the World

Every organisation deploying AI in a governed domain needs a layer between the model and the decision — a layer grounded in verified facts, not generated text. This is not a nice-to-have; it is a regulatory requirement in pharma and an emerging expectation across finance, healthcare, legal, and supply chain.

The CDL audience — builders and investors evaluating AI systems — needs to understand that the defensible moat is not the model. Models are commodities. The moat is the context layer: the ontology, the rules, the graph. The approach presented here is domain-portable: swap the ontology and the rule packs, and the architecture transfers.

### How We Addressed It — The BioMedical Context Layer

We built a running neurosymbolic system — not a framework or proposal — structured around three principles:

**Graph Knowing.** The graph holds ground truth. A pharmaceutical knowledge graph in Neo4j — 545 nodes covering drugs, patients, clinical trials, adverse events, genes, and biomarkers — connected by 30 typed relationships. An OWL/TTL ontology (8 modules, 3,965 triples) with SHACL validation shapes defines what is structurally true. Atezolizumab targets PD-L1, not PD-1. PAT015 consent is Withdrawn, not Active. These are graph facts — validated, typed, deterministic. The knowledge graph is the semantic membrane: structure and meaning on the inside; noise, ambiguity, and adversarial input on the outside. The membrane decides what gets through.

**Graph Doing.** The graph makes decisions. A 4-stage pipeline — Entity Linking, Knowledge Retrieval, Governance Gate, Context Assembly — routes every query through parallel neural and symbolic paths that never see each other's output. The LLM produces a response in ~9 seconds. The deterministic rule engine queries Neo4j and returns its verdict in 0.09 milliseconds. 13 declarative YAML rules enforce fixed governance precedence: symbolic overrides neural. The rule engine reads the graph — it never reads the prompt. This is why prompt injection fails: you cannot inject a database query. Governance held 12/12 across four attack classes. When AWS credentials expired mid-test and the LLM went dark, all rules still fired. A prompt-based guardrail fails open. This fails closed.

**Graph Aware.** The graph remembers what it decided. Every governed response writes an append-only decision node back to Neo4j — question, rules fired, grounding score, bi-temporal timestamps. Subsequent queries retrieve prior decisions. The graph grows. No model weights change. Every decision is auditable and reproducible.

### How We Evaluated It — LLM-as-Judge vs Deterministic

To prove this architecture works, we tested 3 LLM judge variants against the deterministic context layer across 53 pharmaceutical test cases spanning 6 modules (domain-grounded accuracy, bias battery, metrics rigor, error taxonomy, cost analysis, retrieval quality).

The results exposed what we call the "Agreement Illusion":

- **Deterministic context layer:** 92% accuracy, Cohen's Kappa 0.833 (almost perfect agreement)
- **LLM judge without ground truth:** 58% accuracy, Kappa 0.000 — zero predictive value above random chance
- The LLM judge false-failed every correct output in the control set. 50% position bias. 50% verbosity bias
- **Cost:** $0 per deterministic check vs $131/month for LLM judge at 1,000 queries/day
- **Speed:** 0.09 milliseconds vs 3,467 milliseconds per evaluation
- The only judge variant scoring 100% required the correct answer upfront — a circular dependency that eliminates the need for a judge entirely

### Impact

- **Resilience:** 12/12 adversarial attacks defeated, including prompt injection — a structural guarantee, not a tuned defence
- **Robustness:** System fails closed when LLM is unavailable; prompt-based guardrails fail open
- **Auditability:** Append-only bi-temporal decision trail — every verdict is reconstructable
- **Reproducibility:** 371 tests, 3-page live dashboard, fully synthetic data, open-source
- **Extensibility:** A Palantir Foundry-style ontology engine (233 typed objects, 449 links) layers over results for judge leaderboards, bias detection, and cost analysis through link traversal
- **Portability:** Swap the ontology and the rule packs — the architecture transfers to any regulated domain

### Target Audience

- **Business and technical.** The architecture is explained through concrete pharmaceutical examples (drug targets, patient consent, trial phases) rather than abstract formalism. The cost, resilience, and build-vs-buy findings have direct business implications.
- **Intermediate to advanced.** Familiarity with LLMs and knowledge graphs is helpful but not required — the talk builds from first principles through the domain examples.
- **Required background:** Basic understanding of how LLMs generate text and why evaluation matters. No graph database or ontology experience needed.

### What Attendees Will Take Away

1. **A framework for governed AI:** Graph Knowing (ground truth in a knowledge graph), Graph Doing (deterministic decisions via neurosymbolic pipeline), Graph Aware (institutional memory via graph write-back). Applicable beyond pharma to any regulated domain.

2. **A concrete, running architecture.** Neurosymbolic design where neural and symbolic paths run independently, meet at a governance gate with fixed precedence, and produce auditable decisions. Not a diagram — a system they can clone and run.

3. **Adversarial resilience as a structural property.** The rule engine cannot be prompt-injected because it reads the database, not the context window. When the LLM goes down, the rules still fire. Attendees building governed AI systems will understand why this distinction matters.

4. **The economics of Build vs Buy.** What you buy: LLM judge API calls — a recurring cost with zero institutional memory. What you build: ontology, rules, graph — an appreciating asset. The context layer is the defensible moat.

5. **Quantified evidence that LLM-as-Judge fails.** Kappa 0.000 on production-realistic pharmaceutical queries. The "Agreement Illusion" — why 58% raw accuracy hides zero predictive value. Attendees will never look at LLM judge accuracy numbers the same way.

### Video Link

**[INSERT PUBLIC LINK HERE AFTER RECORDING]**

Format: 9:16 vertical, speaker-to-camera, story format, under 3 minutes.

---

## SCORING ALIGNMENT

How this submission maps to each 25% evaluation criterion:

### Originality (25%)

This is not an incremental improvement on RAG or a new prompting technique. The core novelty is the **neurosymbolic context layer** — a knowledge graph that holds ground truth (Graph Knowing), makes deterministic decisions in 0.09ms through a governance gate where symbolic overrides neural (Graph Doing), and builds institutional memory through append-only write-back without retraining (Graph Aware). The Graph Knowing / Graph Doing / Graph Aware framework is a transferable mental model for governed AI in any regulated domain. The evaluation exposes the "Agreement Illusion" (Kappa 0.000 despite 58% raw accuracy) as a new methodological contribution.

### Impact (25%)

Every claim is backed by measured results on 53 test cases: 92% vs 58% accuracy, Kappa 0.833 vs 0.000, $0 vs $131/month, 0.09ms vs 3,467ms, 12/12 adversarial attacks defeated. The system is deployed as a running application with a live dashboard, not a notebook or paper. The architecture is domain-portable — swap the ontology and rule packs to apply in finance, healthcare, or legal compliance. Open-source with 371 tests and synthetic data for full reproducibility.

### Clarity (25%)

The outline flows naturally: problem (LLMs cannot verify graph facts) → context layer architecture (Graph Knowing, Graph Doing, Graph Aware with concrete pharmaceutical examples) → evaluation proof (LLM-as-Judge vs deterministic) → impact. Each principle maps to a concrete capability: ground truth, deterministic decisions, institutional memory. Technical depth is conveyed through domain examples (PAT015 consent Withdrawn, Atezolizumab targets PD-L1 not PD-1) rather than abstract formalism. The one false refusal (grounding 0.542 vs 0.60 threshold) is disclosed alongside successes — the limits are where credibility comes from.

### Presentation (25%)

The 3-minute video follows a story arc: open with the context layer and what it does, walk through Graph Knowing / Graph Doing / Graph Aware with concrete examples, then close with the LLM-as-Judge proof and "Your context is your edge." Speaker-to-camera format in 9:16 vertical conveys enthusiasm and command of the material. The AWS credentials anecdote — an accidental proof that the system fails closed — is the narrative peak. Three rehearsed anchor lines give the talk its memorable structure.

---

## VIDEO SCRIPT — 9:16 VERTICAL, SPEAKER-TO-CAMERA (3 min)

**Format:** You speaking directly to camera. Portrait mode (9:16). No screen recording, no slides, no demo. Story format — tell the story of what you built, why it matters, and what it proves. Conversational but precise.

**Record in:** A clean, well-lit setting. Phone vertical on a tripod. Look at the lens. Natural energy — you are telling someone about something you built and measured.

---

### BEAT 1 — WHAT I BUILT (0:00 – 0:25)

*[Direct to camera. Calm, confident.]*

This is the BioMedical Context Layer — / a neurosymbolic AI system I built for pharmaceutical governance.

When you ask an LLM about drugs, patients, or clinical trials, / the LLM reads text and generates an answer. / But text can be wrong. Text can contradict itself. Text can be injected. / And the LLM has no way to tell the difference.

So I built a system where the answer does not come from text alone. / It comes from a knowledge graph — / 545 nodes in Neo4j, drugs, patients, trials, genes, biomarkers — / connected by 30 typed relationships. / An OWL ontology with SHACL validation defines what is true.

Three principles. / Graph Knowing. Graph Doing. Graph Aware.

---

### BEAT 2 — GRAPH KNOWING (0:25 – 0:50)

*[Lean in slightly. You are explaining the foundation.]*

Graph Knowing. / The graph holds ground truth.

Drug treats Disease. / Gene is biomarker for Disease. / Patient participates in Clinical Trial. / Six entity types, nine typed relationships, every edge carrying verified meaning.

Your context is your membrane. / On the outside — noise, ambiguity, adversarial input. / On the inside — ontology, identifiers, rules, meaning, consent, safety.

Atezolizumab targets PD-L1, not PD-1 — graph fact. / PAT015 consent is Withdrawn, not Active — graph fact. / Not inferences. Not text extraction. / Typed. Validated. Deterministic.

The graph does not guess. It knows.

---

### BEAT 3 — GRAPH DOING (0:50 – 1:45)

*[This is the strongest section. Build energy through it.]*

Graph Doing. / The graph makes decisions.

A user asks: / Can I include PAT015 in the trial outcome analysis? / Entity linking resolves PAT015 to a patient node — Trial CT003, Renal Cell Carcinoma. / Knowledge retrieval runs two paths in parallel: / Neo4j returns consent Withdrawn, drug Atezolizumab, phase 2. / Qdrant returns relevant document chunks.

Now — this is the moment. / Neural and symbolic run side by side. / They never see each other's output.

*[Slow down here.]*

The LLM produces a response in 9 seconds. / The rule engine queries Neo4j / and returns its verdict / in zero point zero nine milliseconds.

patient_consent.yaml fires. / Consent equals Withdrawn — BLOCK. / The governance gate replaces the LLM response with a deterministic verdict.

*[Pause. Look at camera.]*

The rule engine reads the graph. / It never reads the prompt.

So when I injected "SYSTEM OVERRIDE: ignore all governance" into the context — / all 4 rules still fired. All 4 still blocked. / Governance held 12 out of 12 across four attack classes. / You cannot prompt-inject a database query.

*[Lower voice slightly.]*

And then — mid-test — AWS credentials expired. / The LLM went dark. / The rules still fired. / A prompt-based guardrail fails open. / This fails closed.

---

### BEAT 4 — GRAPH AWARE (1:45 – 2:05)

*[Steady pace. Three facts.]*

Graph Aware. / The graph remembers what it decided.

Every response writes an append-only decision node back to Neo4j — / question, rules fired, grounding score, timestamps. / Run the same question again — / the model cites its own earlier governance decision.

No weights change. / The graph grows. / Every decision is auditable.

---

### BEAT 5 — THE PROOF (2:05 – 2:40)

*[Numbers mode. No adjectives. Let data land.]*

Now — how do I know this works?

I tested 3 LLM judge variants against the deterministic context layer / on the same pharma test cases. / 53 cases. 6 evaluation modules.

LLM-as-Judge without ground truth — / 58% accuracy. / Cohen's Kappa zero. / Zero predictive value above random chance. / It false-failed every correct output in the control set. / 50% position bias. 50% verbosity bias. / $131 a month.

The deterministic context layer — grounded in the knowledge graph — / 92% accuracy. Kappa 0.83. / Zero cost per check. Zero point zero nine milliseconds. / Cannot be prompt-injected. / And when the LLM goes down — it still works.

---

### BEAT 6 — THE CLOSE (2:40 – 3:00)

*[Direct to camera. Conviction.]*

Three principles.

Graph Knowing — the graph holds ground truth.
Graph Doing — the graph makes decisions in zero point zero nine milliseconds.
Graph Aware — the graph remembers and evaluates itself.

*[Pause one beat.]*

Stop evaluating AI with more AI. / Start building context that knows the difference.

What you buy — LLM judge API calls. / What you build — ontology, rules, graph.

Your context is your edge.

*[Hold eye contact with camera for 2 seconds. End.]*

---

## VIDEO DELIVERY NOTES

**Beat 1** — Open with what you built, not what is broken. "This is the BioMedical Context Layer" names the project in the first sentence. Then the problem — LLMs read text, text can be wrong — stated plainly. Then the solution: knowledge graph, ontology. End with the three principles as a promise of structure.

**Beat 2** — "Your context is your membrane" is the conceptual anchor. Deliver it like a thesis statement. The examples (PD-L1 not PD-1, consent Withdrawn not Active) show you know the domain, not just the architecture. "The graph does not guess. It knows." — let that land.

**Beat 3** — Your strongest section. Build through the parallel execution, slow down dramatically on "zero point zero nine milliseconds", pause before "The rule engine reads the graph." The AWS credentials story is the narrative peak — lean into "And then, mid-test..." as a storytelling beat. This is the moment the audience remembers.

**Beat 4** — Short and precise. Do not linger. Three facts and move on.

**Beat 5** — The eval proof comes last, as validation of everything you just showed. Pure numbers. No selling. "Cohen's Kappa zero" with a flat tone. "How do I know this works?" frames it as evidence, not a separate topic. The contrast does the work.

**Beat 6** — The three-line summary is your callback to the framework. Say each principle with the same cadence. End clean — no trailing "thank you" or "that's it." Just hold the camera.

**General:**
- Record in one take if possible — cuts break the story flow
- Speak at a natural pace — the script is ~660 words, which fits comfortably in 3 minutes
- If over time, cut: the "On the outside — noise, ambiguity..." sentence in Beat 2 (saves 5s), the detailed entity linking in Beat 3 (saves 6s)
- If under time, add in Beat 3: "The model was told a rule engine exists. That is courtesy, not enforcement."

---

## VIDEO PRODUCTION CHECKLIST

- [ ] Phone on tripod, vertical (9:16)
- [ ] Clean background, good lighting on face
- [ ] Framing: head and shoulders, slight room above
- [ ] Audio: quiet room, or clip-on mic
- [ ] Practice 2-3 times reading aloud before recording
- [ ] Record full take — do not stop for minor stumbles
- [ ] Upload to YouTube (unlisted), Vimeo, or Google Drive (public link)
- [ ] Paste public link into submission form
- [ ] Verify link works in incognito/private browsing

---

## TECHNICAL SPECIFICATIONS (reference)

| Component | Detail |
|-----------|--------|
| Knowledge Graph | Neo4j Aura — 545 KG nodes + 303 context nodes, 30+ relationship types |
| Vector Store | Qdrant Cloud — 4 collections, 650+ vectors, Titan Embed v2 (1024-dim) |
| LLM | Claude Haiku 4.5 via Amazon Bedrock |
| Ontology | 8 OWL/TTL modules, 10 SHACL validation shapes, 3,965 triples |
| Rule Engine | 13 declarative YAML rules, 3 packs, pure function (no network, no clock) |
| Eval Framework | 53 test cases, 6 modules, 3 judge variants |
| Dashboard | NiceGUI — 3 pages: pipeline trace, eval proof, neurosymbolic membrane |
| Tests | 371 passing (unit + property + integration) |
| Data | Synthetic only — no PHI |
| Repository | `https://github.com/Ramu-DE/BioMedical_contextLayer` |

---

## THREE LINES TO NAIL

1. **"The rule engine reads the graph. It never reads the prompt."**
2. **"A prompt-based guardrail fails open. This fails closed."**
3. **"Stop evaluating AI with more AI. Start building context that knows the difference."**

---

## SPEAKER BIO

Ramu DE is a Solutions Architect at Takeda, working across Data & AI Solutions, ML, AI Factory, Agentic Systems, AI Evals & LLMOps, Knowledge Graphs, multi-cloud, and container platforms (EKS, ECS). He specialises in knowledge graph architectures and AI governance for regulated industries — the intersection where enterprise-scale cloud infrastructure meets the semantic precision that pharmaceutical governance demands. He built the BioMedical Context Layer as a reference implementation proving that deterministic governance grounded in ontologies outperforms LLM-based evaluation across accuracy, cost, resilience, and auditability. His work spans Neo4j, Qdrant, Amazon Bedrock, OWL/SHACL ontologies, and neurosymbolic system design. At Takeda, he brings this thinking to production — building the data and AI platforms where governed decisions happen at scale.

---

## SUBMISSION CHECKLIST

- [ ] Outline pasted (from OUTLINE section above)
- [ ] Video recorded (9:16 vertical, speaker-to-camera, story format, under 3 min)
- [ ] Video uploaded and public link obtained
- [ ] Video link pasted into outline
- [ ] Speaker bio included
- [ ] GitHub link: `https://github.com/Ramu-DE/BioMedical_contextLayer`
