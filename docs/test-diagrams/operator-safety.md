# Operator safeguards and authorized benign live exercises: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

**KPI / PM events:** use each TC ID in the [case-focus table](../kpi-pm.md#case-specific-focus-checks), plus all measurement/event groups inherited from its acceptance profiles. Actual collector names and thresholds need approval; local event labels are not standardized counters.

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-041

**What you test:** Benign live detection/tracking confirmation.

**Setup:** approved `M/R/V` subset. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Authorized cooperative non-weaponized<br/>aircraft within permitted envelope"]
    exercise["Exercise: Benign live detection/tracking confirmation.<br/>Test boundary: Separately approved benign live exercise;<br/>no response actuation"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; track<br/>continuity, identity swaps, age and reacquisition time;<br/>session availability, loss, latency and throughput;<br/>authorization, interlocks, stop deadlines and safe state.<br/>Retain: E1,E2,E3,E6"]
    checks["Check: independent truth and service bounds; no response<br/>actuation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S6. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-TRK,A-COM,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S1,S2,S3,S6; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-SAF.

## TC-042

**What you test:** Uninvolved aircraft/person or boundary incursion.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Tabletop rehearsal; live stop<br/>observation only if independently safe"]
    exercise["Exercise: Uninvolved aircraft/person or boundary<br/>incursion. Test boundary: Tabletop workflow; live<br/>observation only if independently safe"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state. Retain: E6"]
    checks["Check: execute approved abort plan without pursuing or<br/>interacting with uninvolved aircraft"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S5,S6. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S5,S6; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF.

## TC-043

**What you test:** Exercise permission or operator-control loss.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Tabletop/mocked loss notification; no<br/>deliberate live control loss"]
    exercise["Exercise: Exercise permission or operator-control loss.<br/>Test boundary: Tabletop / mocked permission and control-<br/>loss workflow"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state; alarm delivery,<br/>acknowledgement, decisions and operator workload. Retain:<br/>E4,E6"]
    checks["Check: independent stop authority and responsible operator<br/>receive correct escalation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S5,S6. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF,A-HUM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S5,S6; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF,REQ-HUM.

## TC-044

**What you test:** Human ambiguity and uncertainty display.

**Setup:** `X/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Recorded unknown/conflicting scenes<br/>in operator simulator"]
    exercise["Exercise: Human ambiguity and uncertainty display. Test<br/>boundary: Operator workflow and disconnected mocks"]
    capture["Measure against approved truth / fixtures:<br/>unknown/ambiguous decisions and confidence calibration;<br/>alarm delivery, acknowledgement, decisions and operator<br/>workload. Retain: E1,E6"]
    checks["Check: display age, confidence, disagreement and missing<br/>identity without hostility inference"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-UNC,A-HUM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-UNC,REQ-HUM.

## TC-045

**What you test:** Alarm burst and operator handover.

**Setup:** `Q/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded synthetic alarms in tabletop<br/>simulator"]
    exercise["Exercise: Alarm burst and operator handover. Test<br/>boundary: Operator workflow and disconnected mocks"]
    capture["Measure against approved truth / fixtures: alarm delivery,<br/>acknowledgement, decisions and operator workload;<br/>authorization, interlocks, stop deadlines and safe state.<br/>Retain: E4,E6"]
    checks["Check: preserve priority, ownership and acknowledgement<br/>under approved workload"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-HUM,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-HUM,REQ-SAF.

## TC-046

**What you test:** Missing/expired authorization for mocked response.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic requests to disconnected<br/>response simulator"]
    exercise["Exercise: Missing/expired authorization for mocked<br/>response. Test boundary: Operator workflow and<br/>disconnected mocks"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state; freshness,<br/>ordering, validation, access and audit completeness.<br/>Retain: E5,E6"]
    checks["Check: deny request; record reason and actor; no real<br/>effector interface"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF,REQ-DAT.

## TC-047

**What you test:** Human approval absent or withdrawn.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock operator workflow with approval<br/>withheld/revoked"]
    exercise["Exercise: Human approval absent or withdrawn. Test<br/>boundary: Operator workflow and disconnected mocks"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state; alarm delivery,<br/>acknowledgement, decisions and operator workload. Retain:<br/>E6"]
    checks["Check: no automated engagement and no action after<br/>withdrawal"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF,A-HUM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF,REQ-HUM.

## TC-048

**What you test:** Stop/interlock failure or lost controller heartbeat.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated mock interface with<br/>independent test cutoff"]
    exercise["Exercise: Stop/interlock failure or lost controller<br/>heartbeat. Test boundary: Operator workflow and<br/>disconnected mocks"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E4,E6"]
    checks["Check: unavailable control inhibits outputs and<br/>independent stop remains effective"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF,REQ-RES.

## TC-049

**What you test:** Authorized responder notification and handoff.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock notification and tabletop<br/>responder coordination"]
    exercise["Exercise: Authorized responder notification and handoff.<br/>Test boundary: Operator workflow and disconnected mocks"]
    capture["Measure against approved truth / fixtures: alarm delivery,<br/>acknowledgement, decisions and operator workload;<br/>freshness, ordering, validation, access and audit<br/>completeness. Retain: E5,E6"]
    checks["Check: uncertainty/provenance retained; no claim that<br/>notification equals protection"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-HUM,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-HUM,REQ-DAT.

## TC-050

**What you test:** Evidence retention, access and privacy.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic incident artifacts and<br/>approved retention-policy fixtures"]
    exercise["Exercise: Evidence retention, access and privacy. Test<br/>boundary: Operator workflow and disconnected mocks"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness.<br/>Retain: E5,E6"]
    checks["Check: least-authorized access, integrity verification and<br/>retention/deletion rules demonstrated"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT.
