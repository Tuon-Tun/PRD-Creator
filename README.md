# Automated PRD Writing Pipeline Operation Guide

This document provides instructions on how to use the PRD Writer tool and details the operational workflow, helping newcomers understand how the system works and how to interact with it to achieve the best quality results.

---

## 1. Process Overview (The Automated HITL Pipeline)

The PRD writing process is orchestrated by the **Master PRD Writer** (`prd-writer.md`), which helps transform raw user requirements into a complete, standard PRD document that can be exported to a DOCX file.
**BPMN Warning:** Inform the user that BPMN is token-heavy and output is "Basic" (manual coordinate estimation).
The process consists of 6 main steps with human intervention at critical decision points (Human-in-the-loop - HITL):

### Step 0: Diagram Requirement Confirmation (Clarification)

- The system will determine whether the feature requires the use/drawing of Diagrams (BPMN, Activity, Sequence).
- *Note* Don't try
- If you haven't mentioned it, the system is strictly required to pause and ask you for the desired diagram types to plan accordingly.

### Step 1: Data Pre-processing (Input Router)

- Your raw request is passed through the `input-router` tool to be standardized into a clear JSON structure (including Feature Name, User Flow, Business Logic, and Edge Cases).
- This raw data is stored according to Domain standards (e.g., `/domain-knowledge/[Domain_Name]/inputs/`).
- **Important Note:** You will be able to review, approve, or add information to this JSON file (especially missing information sections - marked as `[NEEDS_CLARIFICATION]`) before the system moves to the drafting step.

### Step 2: Domain Knowledge & Framework Preparation

- The system will automatically synthesize previous business rules and design principles of the corresponding Domain.
- Strictly apply standards for creating User Stories and JTBDs (ensuring INVEST standards and full coverage of test cases).

### Step 3: Drafting

- Based on the JSON data generated in Step 1, the system creates a draft PRD in Markdown format.
- Stored in the correct `/PRDs/` folder of the Domain.

### Step 4: Quality Assurance (PRD Reviewer)

- The draft is handed over to the `prd-reviewer` - acting as a QA Product Manager - to scrutinize logic flaws, missing edge cases, etc.
- The review comments (*Reviewer's Notes*) will be inserted directly (inline) below the problematic sections in the draft file, proposing solutions and making the comparison process highly visual.

### Step 5: User Approval (CRITICAL PAUSE)

- **The system is MANDATED to pause here for your review.**
- You will provide modification and adjustment requests for the PRD (which already includes Reviewer's Notes). This process repeats until you issue the "Agree" or "Approve" command.

### (Optional) Step 5.5: Wireframe/UI Creation (Stitch MCP)

- Based on the finalized PRD, if there are UI display definitions, the system will call MCP to automatically create the application and generate visual Wireframe/Preview screens.

### Step 6: File Export (Docx Converter)

- Once the "Approve" process is confirmed, the system processes the final Markdown content to export it into a Word file (.docx) and returns the file path to you.

---

## 2. User Guide: "Standard" Input Structure

In reality, the data you provide in **Step 1** determines 80% of the generated PRD's quality. To save time on Q&A and prevent empty generated logic (`[NEEDS_CLARIFICATION]`), users should provide a raw information flow that meets the following basic elements:

1. **Feature Name & Core Objective (Business Value):** What is this feature? What user problem does it solve, or what value does it bring to the business?
2. **Basic User Flow:** How does the happy path happen? Example: Step 1 user clicks button X > Step 2 system displays screen Y.
3. **Logic and Constraints (Business Rules & Edge Cases):** What are the input conditions? What are the conditions for deducting money/adding points/blocking access? If the user loses connection, the system times out, or the balance is empty, what error is displayed?
4. **Diagram Needs:** Clearly state if you want an additional Sequence diagram, BPMN, or Activity Diagram.

**Example of an ideal Input:** > *"Create a Group Lucky Money feature for the Lunar New Year. Objective: increase user engagement. User flow: From main screen -> Select Group Lucky Money -> Enter Greetings, Enter total amount 200k -> Select Random split mode for 10 people -> Click Send -> Share link to group chat -> Users click link to receive random money. Edge case: If the 11th user clicks, report out of turns. If the sender's balance is insufficient when sending => Show pop-up error requesting a deposit. Need to draw a Sequence Diagram."*

The higher the quality of the Input, the more perfect, accurate, and error-free the generated PRD will be.

---

## 3. Note: When NOT to use the entire PRD flow?

The 6-step workflow is highly ideal for large Features (Epics/Features).

However, if the user has a **small project scale**, or **only needs to create single document structures** (For example: You just need to write a few scattered User Stories to create Jira tickets, or outline a JTBD framework), you can **skip this PRD process to save time**.

At that time, consult or request the LLM to directly call the specific Skills that are readily available in these folders:

- **To create Jobs-to-be-Done (JTBD):** Refer to `/knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
- **To create INVEST-standard User Stories:** Refer to `/knowledge-base/knowledge/user-story-skill/SKILL.md`

Điều này đảm bảo luồng công việc của bạn được tinh gọn và tiết kiệm nguồn lực một cách tối đa.
