---
name: prd-writer
description: >
  Write structured PRDs by interviewing the user and filling the standard template. Trigger
  when the user mentions: PRD, product spec, feature spec, requirements doc, user story doc,
  "document this feature", "spec out this idea", "write up requirements", or similar.
---

# PRD Writer Skill

Produce a complete PRD by interviewing the user, then filling `references/prd-template.md`.
Scope: PRD writing only — Dev/QC handoff is a separate skill.

---

## Phase 1 — Interview

Group all questions into one message. Minimum required:

1. Feature name
2. Problem context (current behavior, gap, business motivation)
3. Target user / actor
4. Core user story
5. Acceptance criteria (2–5 conditions)
6. Functional requirements
7. Non-functional requirements
8. Success metrics (KPIs + targets)

Optional (ask only if relevant): API endpoints, UI/UX details, JTBD emotional/social jobs.
**Diagrams (MANDATORY TO ASK):** Explicitly ask the user if they want to generate diagrams, and if yes, WHICH types of diagrams they need (BPMN, Activity Diagram, or Sequence Diagram).

Skip interview if the user provides enough context upfront.

---

## Phase 2 — Draft

Load `references/prd-template.md`. Fill every section; write `TBD` for unknowns.

**Rules:**

- AC: Gherkin format (`Given / When / Then / And`), minimum 3 items.
- FR: assign `High / Medium / Low` priority to every row, minimum 3 rows.
- API specs not provided → mark `[DEV TO COMPLETE]`.
- Use Case table: fill Actor, Pre/Postcondition, Main Flow, Alternative Flow, Exception Flow.
- **Section 3.3** — generate ONLY the diagrams explicitly requested by the user; see rules below.

---

## Phase 3 — Version

Default `0.1` for new docs. Increment (`0.2`, `0.3` …) on each revision. One-line summary in Version History.

---

## Section 3.3 — Diagram Rules

**CRITICAL RULE:** Diagram generation is OPTIONAL. You BẮT BUỘC (MUST) explicitly ASK the user beforehand if they want to draw diagrams, and if yes, WHICH types (BPMN, Activity, and/or Sequence). Only generate the ones they specify. Never use plain text lists or Mermaid for the requested diagrams.

### 3.3.1 BPMN — bpmn.io XML

- Output a ```xml fenced block containing valid BPMN 2.0 XML (see template skeleton).
- Required elements: `<collaboration>` pool → `<process>` with `<laneSet>` → one `<lane>` per actor → `<sequenceFlow>` for every connection → `<bpmndi:BPMNDiagram>` with `<dc:Bounds>` per shape and `<di:waypoint>` per edge.
- One lane each for: User, App/Frontend, Backend Service (add more if needed).
- Layout: pool label column 30 px; task 120×80, startEvent/endEvent 36×36, gateway 50×50; User lane height 120–130 px, App lane 200–220 px, each backend lane ≥ 100 px.
- Cross-lane tasks that communicate should align vertically for clean edges.
- Use `&amp;` for `&` in XML `name` attributes.

### 3.3.2 Activity Diagram — PlantUML

- Output a ```plantuml fenced block (see template skeleton).
- Must include: happy path + ≥ 1 alternative branch + ≥ 1 error/exception branch.
- Step labels ≤ 8 words. No swimlanes (BPMN handles that).

### 3.3.3 Sequence Diagram — PlantUML

- Output a ```plantuml fenced block (see template skeleton).
- Use `->` for requests, `-->` for responses. Wrap paths in `alt / else / end`.
- Name every external service as a participant (Auth, Analytics, DB, etc.).
- Annotate every arrow with HTTP method + endpoint or action name.

---

## Quality Checklist

- All template section headers present.
- Section 3.3: only diagrams specifically requested by the user are generated.
- No blank sections (use `TBD`).
- Language matches the user (English or Vietnamese).
