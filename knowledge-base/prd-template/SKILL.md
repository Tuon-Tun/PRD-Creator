---
name: prd-template-renderer
description: >
  Render a full PRD from an approved structured brief and domain context. Use when the
  orchestrator has already collected and approved the feature JSON and needs the standard PRD
  filled end-to-end without re-interviewing the user.
---

# PRD Template Renderer

Produce a complete PRD from an approved structured brief, then fill `resources/prd-template.md`.
Scope: PRD drafting only. Review and export are separate steps in the pipeline.

---

## Phase 1 - Inputs

Before drafting, confirm you have:

1. The approved JSON brief from Step 1
2. Domain context from `/domain-knowledge/[Domain_Name]/rules.md`
3. Relevant domain history from prior PRDs or inputs, if present
4. Standards from:
   - `/knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
   - `/knowledge-base/knowledge/user-story-skill/SKILL.md`

Do not re-interview the user if the orchestrator already completed the approval step. Only stop and request clarification if a critical field remains blocked after Step 1 approval.

---

## Phase 2 - Draft

Load `resources/prd-template.md`. Fill every section. Use `TBD` only when the approved brief still contains an unresolved gap.

**Rules:**

- Acceptance Criteria must follow the `Done when` standard from `user-story-skill`.
- Apply JTBD and user-story standards strictly; do not shortcut them to save tokens.
- Functional Requirements must include a `High / Medium / Low` priority.
- API details not provided -> mark `[DEV TO COMPLETE]`.
- Use Case tables must include Actor, Precondition, Postcondition, Main Flow, Alternative Flow, and Exception Flow.
- Section 3.3 must include only the diagram types explicitly approved by the user.
- Keep `Version History` and `References` tables present but unfilled.

---

## Phase 3 - Versioning

Default to `0.1` for new documents. Increment (`0.2`, `0.3`, and so on) only if the workflow explicitly requires it. Do not invent change history if the table is meant to stay unfilled.

---

## Section 3.3 - Diagram Rules

**Critical rule:** Diagram generation is optional. Only generate the diagram types explicitly approved by the user in Step 0 or Step 1. Never substitute plain text or Mermaid when BPMN, Activity Diagram, or Sequence Diagram is requested.

### 3.3.1 BPMN - bpmn.io XML

- Output a ```xml fenced block containing valid BPMN 2.0 XML (see template skeleton).
- Required elements: `<collaboration>` pool -> `<process>` with `<laneSet>` -> one `<lane>` per actor -> `<sequenceFlow>` for every connection -> `<bpmndi:BPMNDiagram>` with `<dc:Bounds>` per shape and `<di:waypoint>` per edge.
- One lane each for: User, App/Frontend, Backend Service (add more if needed).
- Layout: pool label column 30 px; task 120x80, startEvent/endEvent 36x36, gateway 50x50; User lane height 120-130 px, App lane 200-220 px, each backend lane >= 100 px.
- Cross-lane tasks that communicate should align vertically for clean edges.
- Use `&amp;` for `&` in XML `name` attributes.

### 3.3.2 Activity Diagram - PlantUML

- Output a ```plantuml fenced block (see template skeleton).
- Must include: happy path + at least 1 alternative branch + at least 1 error or exception branch.
- Step labels must stay under 8 words. No swimlanes.

### 3.3.3 Sequence Diagram - PlantUML

- Output a ```plantuml fenced block (see template skeleton).
- Use `->` for requests and `-->` for responses. Wrap success versus error paths in `alt / else / end`.
- Name every external service as a participant (Auth, Analytics, DB, and so on).
- Annotate every arrow with an HTTP method + endpoint or an explicit action name.

---

## Quality Checklist

- All template section headers are present.
- Section 3.3 contains only the diagrams explicitly requested by the user.
- No blank sections remain; use `TBD` when information is still pending.
- The language matches the user.
