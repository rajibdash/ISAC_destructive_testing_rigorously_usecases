# Device-RAN-core-AI compound failures and end-to-end assurance: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

**KPI / PM events:** use each TC ID in the [case-focus table](../kpi-pm.md#case-specific-focus-checks), plus all measurement/event groups inherited from its acceptance profiles. Actual collector names and thresholds need approval; local event labels are not standardized counters.

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-113

**What you test:** Observation-to-operator latency/freshness under concurrent load.

**Setup:** `C/B/J/M/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Timestamped scene replay with device,<br/>RAN, transport, core, AI and mock consumer spans"]
    exercise["Exercise: Observation-to-operator latency/freshness under<br/>concurrent load. Test boundary: Device / RAN / core / AI /<br/>mock consumer"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency; alarm delivery, acknowledgement, decisions and<br/>operator workload; session availability, loss, latency and<br/>throughput. Retain: E1,E2,E6,E7,E8"]
    checks["Check: meet end-to-end and per-hop budgets including<br/>queues/retries; a timely stale result fails"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S3,S5. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-AI,A-HUM,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S2,S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-AI,REQ-HUM,REQ-COM.

## TC-114

**What you test:** AI-serving burst plus UE registration/session surge.

**Setup:** `C/B/J/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Concurrent bounded synthetic<br/>workloads on declared shared platform"]
    exercise["Exercise: AI-serving burst plus UE registration/session<br/>surge. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; AI quality, abstention, calibration,<br/>numerical validity and latency; session availability,<br/>loss, latency and throughput. Retain: E2,E4,E7,E8"]
    checks["Check: preserve approved isolation/priority and report<br/>rejected/expired work by class"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-AI,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-AI,REQ-COM.

## TC-115

**What you test:** Core disconnection plus continued local observations.

**Setup:** `C/J/U=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Network emulator partition with<br/>timestamped replay at RAN/device"]
    exercise["Exercise: Core disconnection plus continued local<br/>observations. Test boundary: Device / RAN / core / AI /<br/>mock consumer"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>fault isolation, degraded state, restoration and rollback;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E4,E7,E8"]
    checks["Check: only qualified local fallback runs; unavailable<br/>core AI is not reported as active"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-RES,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-RES,REQ-UNC.

## TC-116

**What you test:** Reconnection backlog plus changed model/policy.

**Setup:** `C/B/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Release buffered replay after<br/>isolated update and outage"]
    exercise["Exercise: Reconnection backlog plus changed model/policy.<br/>Test boundary: Device / RAN / core / AI / mock consumer"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency; control permissions, scope/expiry, stability and<br/>stop precedence. Retain: E1,E4,E7,E8,E9"]
    checks["Check: validate age/version/authorization before replay;<br/>no retrospective live-looking decision or old command"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-AI,A-CTL. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-AI,REQ-CTL.

## TC-117

**What you test:** Shared core/AI cluster, storage or region loss.

**Setup:** `C/N/J=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Common-cause service-failure emulator<br/>with synthetic accepted work"]
    exercise["Exercise: Shared core/AI cluster, storage or region loss.<br/>Test boundary: Device / RAN / core / AI / mock consumer"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; fault isolation, degraded state, restoration<br/>and rollback; session availability, loss, latency and<br/>throughput. Retain: E2,E4,E7,E8,E9"]
    checks["Check: demonstrate actual failure-domain independence or<br/>explicitly report correlated loss"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-RES,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-RES,REQ-COM.

## TC-118

**What you test:** Uncertain AI result plus failed operator delivery.

**Setup:** `C/J/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Ambiguous replay and unavailable mock<br/>notification path"]
    exercise["Exercise: Uncertain AI result plus failed operator<br/>delivery. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures:<br/>unknown/ambiguous decisions and confidence calibration;<br/>alarm delivery, acknowledgement, decisions and operator<br/>workload; authorization, interlocks, stop deadlines and<br/>safe state. Retain: E1,E4,E6,E8"]
    checks["Check: retain uncertainty and visible delivery failure; no<br/>automation that bypasses human authority"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-UNC,A-HUM,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-UNC,REQ-HUM,REQ-SAF.

## TC-119

**What you test:** Revocation during active inference/federation.

**Setup:** `C/J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic consent/authorization<br/>withdrawal with in-flight jobs and caches"]
    exercise["Exercise: Revocation during active inference/federation.<br/>Test boundary: Device / RAN / core / AI / mock consumer"]
    capture["Measure against approved truth / fixtures: identity/tenant<br/>binding, track lineage and access decisions;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion; admission/completion/rejection,<br/>queues, retries and state consistency. Retain: E5,E7,E8,E9"]
    checks["Check: enforce approved propagation deadline at result<br/>delivery and onward sharing, not only ingestion"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-ID,A-GOV,A-CORE. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-ID,REQ-GOV,REQ-CORE.

## TC-120

**What you test:** Device/RAN timing/calibration loss plus AI confidence.

**Setup:** `C/J/R/G=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated health/clock faults with<br/>held-out replay"]
    exercise["Exercise: Device/RAN timing/calibration loss plus AI<br/>confidence. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3,E7,E8"]
    checks["Check: propagate invalidity end-to-end even when<br/>classifier score remains high"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-AI,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-AI,REQ-UNC.

## TC-121

**What you test:** Tenant pressure plus core/AI scale-in/failover.

**Setup:** `C/B/J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic multi-tenant load with<br/>controlled isolated rescheduling"]
    exercise["Exercise: Tenant pressure plus core/AI scale-in/failover.<br/>Test boundary: Device / RAN / core / AI / mock consumer"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; identity/tenant binding, track lineage and<br/>access decisions; AI quality, abstention, calibration,<br/>numerical validity and latency. Retain: E2,E4,E7,E8,E9"]
    checks["Check: no cache/result/authority cross-binding and no<br/>hidden resource-budget breach"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4,S7. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-ID,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S1,S2,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-ID,REQ-AI.

## TC-122

**What you test:** Model update plus radio/mode/core API transition.

**Setup:** `C/J/M/R/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Supported directed transitions and<br/>incompatible version fixtures in SIL/HIL"]
    exercise["Exercise: Model update plus radio/mode/core API<br/>transition. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>calibration residuals, clock drift and equipment health;<br/>admission/completion/rejection, queues, retries and state<br/>consistency; fault isolation, degraded state, restoration<br/>and rollback. Retain: E1,E3,E7,E8,E9"]
    checks["Check: block incompatible combinations and bound qualified<br/>rollback"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-RAD,A-CORE,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S1,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-RAD,REQ-CORE,REQ-RES.

## TC-123

**What you test:** Stop/revocation during AI-driven network change.

**Setup:** `C/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock change pending while independent<br/>stop or permission withdrawal arrives"]
    exercise["Exercise: Stop/revocation during AI-driven network change.<br/>Test boundary: Device / RAN / core / AI / mock consumer"]
    capture["Measure against approved truth / fixtures: control<br/>permissions, scope/expiry, stability and stop precedence;<br/>authorization, interlocks, stop deadlines and safe state;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E2,E6,E7,E9"]
    checks["Check: stop/revocation precedence persists across retries,<br/>failover and restart"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S5,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CTL,A-SAF,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CTL,REQ-SAF,REQ-RES.

## TC-124

**What you test:** Recovery from mismatched core/model/data backups.

**Setup:** `C/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated restore from versioned<br/>synthetic snapshots with declared recovery objectives"]
    exercise["Exercise: Recovery from mismatched core/model/data<br/>backups. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; AI quality, abstention, calibration,<br/>numerical validity and latency; purpose/residency,<br/>approvals, revocation and retention/deletion; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E4,E5,E7,E8,E9"]
    checks["Check: validate consistency, revoked rights and accepted-<br/>work disposition before readiness"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-AI,A-GOV,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-AI,REQ-GOV,REQ-RES.

## TC-125

**What you test:** Multi-site object handoff versus UE/session mobility.

**Setup:** `C/G/J/U=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Labeled cross-site replay plus<br/>independent synthetic UE mobility"]
    exercise["Exercise: Multi-site object handoff versus UE/session<br/>mobility. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures: identity/tenant<br/>binding, track lineage and access decisions; track<br/>continuity, identity swaps, age and reacquisition time; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency. Retain: E1,E7,E8"]
    checks["Check: correlate only supported evidence; no duplicate<br/>authoritative object or subscriber-to-object identity<br/>shortcut"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-ID,A-TRK,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-ID,REQ-SEN,REQ-AI.

## TC-126

**What you test:** Core/AI privacy controls under evidence-store failure.

**Setup:** `C/J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic incident traces with<br/>unavailable audit/retention endpoint"]
    exercise["Exercise: Core/AI privacy controls under evidence-store<br/>failure. Test boundary: Device / RAN / core / AI / mock<br/>consumer"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion; fault isolation, degraded state,<br/>restoration and rollback. Retain: E4,E5,E8,E9"]
    checks["Check: apply approved deny/degrade rules, restrict<br/>emergency evidence and expose enforcement gaps"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-GOV,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-GOV,REQ-RES.

## TC-127

**What you test:** Long-duration core/AI churn and repeated degraded recovery.

**Setup:** `C/B/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved-duration isolated jobs,<br/>sessions, updates and fault/recovery cycles"]
    exercise["Exercise: Long-duration core/AI churn and repeated<br/>degraded recovery. Test boundary: Device / RAN / core / AI<br/>/ mock consumer"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; AI quality, abstention, calibration,<br/>numerical validity and latency; fault isolation, degraded<br/>state, restoration and rollback; session availability,<br/>loss, latency and throughput. Retain: E2,E4,E7,E8,E9"]
    checks["Check: bound leaks, queue growth, identity drift and<br/>quality/latency regressions over time"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-AI,A-RES,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S1,S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-AI,REQ-RES,REQ-COM.

## TC-128

**What you test:** Pre-approved multi-domain acceptance and operator handoff rehearsal.

**Setup:** all applicable axes. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Replay a versioned scenario pack with<br/>independent domain owners and mock responders"]
    exercise["Exercise: Pre-approved multi-domain acceptance and<br/>operator handoff rehearsal. Test boundary: Device / RAN /<br/>core / AI / mock consumer"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error;<br/>admission/completion/rejection, queues, retries and state<br/>consistency; AI quality, abstention, calibration,<br/>numerical validity and latency; session availability,<br/>loss, latency and throughput; control permissions,<br/>scope/expiry, stability and stop precedence; alarm<br/>delivery, acknowledgement, decisions and operator<br/>workload; authorization, interlocks, stop deadlines and<br/>safe state; purpose/residency, approvals, revocation and<br/>retention/deletion; every metric required by constituent<br/>instances. Retain: E1,E2,E3,E4,E5,E6,E7,E8,E9"]
    checks["Check: all cross-domain contracts pass; unresolved gaps<br/>explicit"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4,S5,S7. Watch<br/>throughout the run; use the approved trigger and safe<br/>action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-CORE,A-AI,A-COM,A-CTL,A-HUM,A-SAF,A-GOV plus every profile required by constituent instances. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S1,S2,S3,S4,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-CORE,REQ-AI,REQ-COM,REQ-CTL,REQ-HUM,REQ-SAF,REQ-GOV.
