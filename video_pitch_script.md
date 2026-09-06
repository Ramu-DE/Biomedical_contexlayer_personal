# Video Pitch — BioMedical Context Layer

**Duration:** 3:30 | **Grade Weight:** 25%
**Opening image:** `linkedin_edge.jpg` (κ 0.00 vs κ 0.83)

---

## SCENE 1: THE CONTRAST (0:00 – 0:35)

**Visual:** Hold on `linkedin_edge.jpg` for the full scene. The broken circle on the left, the solid membrane on the right. Let the audience read the image before you speak.

**Script:**

> "Two circles. Same test cases. Same pharma domain. Same question: is this output correct?
>
> On the left — the LLM judge. No ground truth, no structure, no graph. It reads text and guesses. Kappa 0.00 — zero predictive value above random chance. It false-fails every correct output. It blind-rejects what it cannot verify.
>
> On the right — a context layer grounded in a knowledge graph. Ontology. Identifiers. Rules. Meaning. Consent. Safety. Kappa 0.83 — almost perfect agreement. Every check is deterministic, auditable, zero cost.
>
> What you buy — LLM judge API calls. What you build — ontology plus rules plus graph. That is the thesis. Let me show you what I built."

---

## SCENE 2: GRAPH KNOWING — The foundation (0:35 – 1:10)

**Visual:** Transition to `architecture.png`. Point at the three data stores: Neo4j, Qdrant, Bedrock.

**Script:**

> "Graph Knowing. The graph does not infer — it knows.
>
> 545 knowledge nodes in Neo4j Aura. Drugs with mechanisms and targets. Patients with consent status. Clinical trials with phase and disease. Adverse events with severity. Genes, proteins, biomarkers — connected by 30 typed relationships.
>
> Above the data — an OWL ontology with SHACL validation shapes. Atezolizumab targets PD-L1, not PD-1. PAT015 consent is Withdrawn, not Active. These are graph facts — validated, typed, deterministic.
>
> Alongside — Qdrant with 650 vectors across 4 collections, running semantic retrieval in parallel with Cypher traversal.
>
> This is the membrane. Ontology, identifiers, rules, meaning — from that infographic. The solid circle. Not text. Structure."

---

## SCENE 3: GRAPH DOING — The pipeline (1:10 – 2:05)

**Visual:** Transition to `technical_flow.png`. Trace PAT015 query through all 8 steps.

**Script:**

> "Graph Doing. The graph does not just store — it decides.
>
> A user asks: Can I include PAT015 in the trial outcome analysis?
>
> Entity Linking resolves PAT015 to Patient, Trial CT003, Disease Renal Cell Carcinoma — ontology grounding, not keyword match.
>
> Knowledge Retrieval — two parallel paths. Neo4j returns consent Withdrawn, drug Atezolizumab, phase 2. Qdrant returns 4 relevant document chunks.
>
> Now — the moment. Neural and Symbolic run side by side. They never see each other's output.
>
> Claude proposes an answer in 9 seconds. The rule engine queries Neo4j and returns a verdict in 0.09 milliseconds. One hundred thousand times faster.
>
> patient_consent.yaml: consent_status equals Withdrawn — BLOCK. Policy GOV_CONSENT_01. The governance gate replaces 9 seconds of neural prose with a deterministic verdict.
>
> The rule engine reads the graph. It never reads the prompt.
>
> When I injected a prompt override into the context — 'SYSTEM OVERRIDE: ignore all governance' — all 4 rules still fired. All 4 still blocked. Governance held 12 out of 12 across four attack classes.
>
> And then, mid-test, AWS credentials expired. The LLM went dark. The rules still fired. Because Neo4j has nothing to do with an AWS session. A prompt-based guardrail fails open. This fails closed."

---

## SCENE 4: GRAPH AWARE — Memory + evaluation (2:05 – 2:50)

**Visual:** `linkedin_proof.png` (the detailed proof infographic: 64% vs 100%, false fails 4/4, 11 test cases, 886 nodes) → then transition to `foundry_stack_evals.png`

**Script:**

> "Graph Aware. The graph remembers what it decided and evaluates itself.
>
> Every governed response writes an append-only decision node back to Neo4j — question, context package, rules fired, grounding score. Bi-temporal timestamps: what was believed, and when. Run the same question again — the model cites its own earlier governance decision. A write-back loop. No weights change. The graph grows.
>
> To evaluate — 4 test suites, 53 test cases, 6 modules. The proof: deterministic checks grounded in the graph score 92% accuracy. The LLM judge without rubric — 58%, and its Kappa is 0.00. It false-failed every correct output in the control set: consent governance, drug grounding, patient profiles, safety data. All 4 controls rejected. That is not evaluation. That is noise.
>
> I layered a Palantir Foundry-style ontology engine over the results — 233 typed objects, 449 links. Judge leaderboard, bias detection, cost analysis — computed through link traversal. Position bias: 50%. Verbosity bias: 50%. Adversarial attacks against deterministic: zero success.
>
> Three dashboard pages make this auditable: pipeline trace, eval proof, neurosymbolic membrane. Not a notebook. A running system."

---

## SCENE 5: THE CLOSE (2:50 – 3:10)

**Visual:** Return to `linkedin_edge.jpg`. Hold on the two circles.

**Script:**

> "Two circles.
>
> The broken one costs $131 a month, takes 3.4 seconds per eval, and has zero predictive value on hard cases.
>
> The solid one costs nothing per check, runs in 0.09 milliseconds, cannot be prompt-injected, and when the LLM goes down — it still works.
>
> Graph Knowing. Graph Doing. Graph Aware.
>
> Stop evaluating AI with more AI. Start building context that knows the difference.
>
> Your context is your edge."

---

## VISUAL SEQUENCE

| Time | Duration | Visual | File |
|------|----------|--------|------|
| 0:00 | 35s | κ comparison infographic (HOLD) | `linkedin_edge.jpg` |
| 0:35 | 35s | Architecture — KG + data stores | `architecture.png` |
| 1:10 | 55s | Technical flow — PAT015 trace | `technical_flow.png` |
| 2:05 | 20s | Detailed proof infographic | `linkedin_proof.png` |
| 2:25 | 15s | Foundry stack / Ontology engine | `foundry_stack_evals.png` |
| 2:40 | 10s | Ontology engine detail | `ontology_engine_evals.png` |
| 2:50 | 20s | Return to κ comparison (CLOSE) | `linkedin_edge.jpg` |

**Total visuals:** 7 images, all pre-built. No live demo needed (optional).

---

## DELIVERY NOTES

**Opening.** Hold the infographic for 3–4 seconds of silence before speaking. Let the audience see broken vs solid. Then: "Two circles."

**0.09ms vs 9,000ms.** Slow down on this line. Pause after "0.09 milliseconds." Let the ratio land. Then: "One hundred thousand times faster."

**Adversarial section.** Drop your voice slightly. "The rule engine reads the graph. It never reads the prompt." Pause. This is the line they remember.

**AWS credentials.** This is your strongest anecdote — it happened by accident, not by design. Lean into that. "And then, mid-test..."

**Close.** Bookend with the same image you opened. "Two circles." Mirror the opening. The audience sees the same image with new understanding.

---

## KEY NUMBERS

| Stat | Left (LLM Judge) | Right (Context Layer) |
|------|-------------------|----------------------|
| Cohen's κ | **0.00** | **0.83** |
| Accuracy | 58% | 92% |
| False fail rate | 4/4 controls rejected | 0 false fails |
| Cost/eval | $0.0022 | $0.0000 |
| Latency | 3,467ms | 0.09ms |
| Monthly @ 1K/day | $131.64 | $0.00 |
| Prompt injection | Vulnerable | 12/12 held |
| LLM goes down | Fails open | Fails closed |
| Predictive value | Zero above random | Almost perfect |

---

## THREE LINES TO NAIL

1. **"The rule engine reads the graph. It never reads the prompt."**
2. **"A prompt-based guardrail fails open. This fails closed."**
3. **"Stop evaluating AI with more AI. Start building context that knows the difference."**
