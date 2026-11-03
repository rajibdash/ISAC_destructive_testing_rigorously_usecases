# AI domain hosted in the core: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-085

**What you test:** Feature/preprocessing contract mismatch.

**Setup:** `C/J/R/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Golden samples plus wrong<br/>unit/order/schema/version fixtures"]
    exercise["Exercise: Feature/preprocessing contract mismatch. Test<br/>boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency. Retain: E1,E5,E8"]
    checks["Check: reject incompatible pipeline versions; no plausible<br/>prediction from misinterpreted features"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-AI.

## TC-086

**What you test:** Missing, truncated or non-finite AI input/output.

**Setup:** `J/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded invalid<br/>tensor/metadata/output fixtures in test adapter"]
    exercise["Exercise: Missing, truncated or non-finite AI<br/>input/output. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency. Retain: E4,E5,E8"]
    checks["Check: explicit validation failure/abstention, no<br/>fabricated class or confidence"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-AI,REQ-UNC.

## TC-087

**What you test:** Inference burst, concurrency and batching.

**Setup:** `C/B/J/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved ramp/burst/hold workloads<br/>from labeled replay"]
    exercise["Exercise: Inference burst, concurrency and batching. Test<br/>boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput. Retain: E1,E4,E7,E8"]
    checks["Check: bound tail latency, oldest-item age and resource<br/>use; explicit overload/expiry"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-CORE,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S1,S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-CORE,REQ-COM.

## TC-088

**What you test:** Accelerator memory pressure, device reset or worker crash.

**Setup:** `C/J=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded allocation load and emulated<br/>runtime faults, no equipment damage"]
    exercise["Exercise: Accelerator memory pressure, device reset or<br/>worker crash. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E4,E8"]
    checks["Check: visible failure and qualified restart/fallback<br/>within approved limits, not invented results"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S1,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-RES.

## TC-089

**What you test:** Cold start/model cache eviction/registry unavailable.

**Setup:** `C/B/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated cache reset and mock model-<br/>store outage"]
    exercise["Exercise: Cold start/model cache eviction/registry<br/>unavailable. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E4,E8,E9"]
    checks["Check: readiness follows verified model loading; report<br/>unavailable during warm-up"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-RES.

## TC-090

**What you test:** Late inference, cancellation and result expiry.

**Setup:** `C/B/J=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Delayed replay jobs and cancelled<br/>requests"]
    exercise["Exercise: Late inference, cancellation and result expiry.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>track continuity, identity swaps, age and reacquisition<br/>time; admission/completion/rejection, queues, retries and<br/>state consistency. Retain: E1,E7,E8"]
    checks["Check: discard or explicitly label late outputs; never<br/>revive cancelled/stale tracks"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-TRK,A-CORE. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-SEN,REQ-CORE.

## TC-091

**What you test:** Out-of-distribution scene/device conditions.

**Setup:** `J/R/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Independently held-out approved<br/>datasets and qualified simulation"]
    exercise["Exercise: Out-of-distribution scene/device conditions.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E8"]
    checks["Check: characterize quality/coverage by stratum and flag<br/>unsupported inputs; no universal OOD-detection guarantee"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-UNC.

## TC-092

**What you test:** Confidence calibration and abstention boundaries.

**Setup:** `J/V/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Versioned evaluation sets across<br/>ambiguity and load strata"]
    exercise["Exercise: Confidence calibration and abstention<br/>boundaries. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E8"]
    checks["Check: meet approved calibration/uncertainty bounds and<br/>abstention policy including timely-output coverage"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-UNC.

## TC-093

**What you test:** Unknown object classes and unsupported identity claims.

**Setup:** `J/P/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Labeled unseen/ambiguous objects and<br/>missing cooperative identity"]
    exercise["Exercise: Unknown object classes and unsupported identity<br/>claims. Test boundary: Declared isolated AI pipeline and<br/>runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>identity/tenant binding, track lineage and access<br/>decisions; unknown/ambiguous decisions and confidence<br/>calibration. Retain: E1,E6,E8"]
    checks["Check: retain unknown class/identity and never infer<br/>hostile intent from score or identity absence"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-ID,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E6: operator actions, mock calls, interlocks and stops; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-ID,REQ-UNC.

## TC-094

**What you test:** Data/concept drift and delayed ground-truth labels.

**Setup:** `J/R/V/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Controlled changes in dataset<br/>composition and label arrival"]
    exercise["Exercise: Data/concept drift and delayed ground-truth<br/>labels. Test boundary: Declared isolated AI pipeline and<br/>runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E1,E8,E9"]
    checks["Check: detect approved measurable drift signals, qualify<br/>monitoring limits and gate continued use/revalidation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-RES.

## TC-095

**What you test:** Training/serving skew and evaluation leakage.

**Setup:** `J/R/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Independent preprocessing comparison<br/>and held-out site/time/object split audit"]
    exercise["Exercise: Training/serving skew and evaluation leakage.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion. Retain: E1,E5,E8,E9"]
    checks["Check: no disallowed split overlap; comparable features<br/>and independently reproduced quality before approval"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-GOV.

## TC-096

**What you test:** Training-data provenance, purpose and residency.

**Setup:** `C/J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic authorized/disallowed<br/>dataset lineage, withdrawal and transfer fixtures"]
    exercise["Exercise: Training-data provenance, purpose and residency.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures:<br/>purpose/residency, approvals, revocation and<br/>retention/deletion; AI quality, abstention, calibration,<br/>numerical validity and latency. Retain: E5,E8,E9"]
    checks["Check: reject unapproved use/transfer; trace affected<br/>derived models and apply approved<br/>requalification/retirement policy, not assumed instant<br/>unlearning"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-GOV,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-GOV,REQ-AI.

## TC-097

**What you test:** Label/data integrity degradation.

**Setup:** `J/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Declared bounded synthetic label<br/>inconsistencies and corrupted records in isolated<br/>evaluation"]
    exercise["Exercise: Label/data integrity degradation. Test boundary:<br/>Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency. Retain: E1,E5,E8,E9"]
    checks["Check: surface integrity/quality failure and block<br/>unqualified model promotion"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-AI,REQ-GOV.

## TC-098

**What you test:** Missing/misaligned modalities at AI fusion.

**Setup:** `J/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Labeled sensor dropout, different<br/>sample rates and alignment errors"]
    exercise["Exercise: Missing/misaligned modalities at AI fusion. Test<br/>boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>track continuity, identity swaps, age and reacquisition<br/>time; unknown/ambiguous decisions and confidence<br/>calibration. Retain: E1,E3,E8"]
    checks["Check: qualified modality-specific degradation or<br/>abstention, with no silent imputation as truth"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-TRK,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-SEN,REQ-UNC.

## TC-099

**What you test:** Correlated/duplicated evidence and ensemble disagreement.

**Setup:** `J/G/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Replay shared-source duplicates and<br/>conflicting approved model outputs"]
    exercise["Exercise: Correlated/duplicated evidence and ensemble<br/>disagreement. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E5,E8"]
    checks["Check: retain lineage and avoid treating correlated<br/>observations as independent certainty"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-DAT,REQ-UNC.

## TC-100

**What you test:** Precision/runtime/hardware portability.

**Setup:** `C/J/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Golden corpus on each approved<br/>CPU/accelerator/quantized runtime"]
    exercise["Exercise: Precision/runtime/hardware portability. Test<br/>boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency.<br/>Retain: E1,E8,E9"]
    checks["Check: meet numerical validity and per-stratum quality<br/>bounds for each qualified artifact/runtime combination"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI.

## TC-101

**What you test:** Model artifact approval/integrity and dependency mismatch.

**Setup:** `J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Test artifacts with invalid digest,<br/>missing approval or incompatible dependency manifest"]
    exercise["Exercise: Model artifact approval/integrity and dependency<br/>mismatch. Test boundary: Declared isolated AI pipeline and<br/>runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion. Retain: E5,E8,E9"]
    checks["Check: refuse activation; retain qualified version only if<br/>permitted and visibly identified"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-GOV.

## TC-102

**What you test:** AI canary/mixed-version rollout and rollback.

**Setup:** `C/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated approved rollout and<br/>deliberately failing evaluation fixture"]
    exercise["Exercise: AI canary/mixed-version rollout and rollback.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>fault isolation, degraded state, restoration and rollback;<br/>identity/tenant binding, track lineage and access<br/>decisions. Retain: E1,E4,E8,E9"]
    checks["Check: bound quality regression, preserve versioned track<br/>lineage and restore qualified model consistently"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-RES,A-ID. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-RES,REQ-ID.

## TC-103

**What you test:** Training versus inference/core resource contention.

**Setup:** `C/B/J/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Quota-limited training/evaluation<br/>jobs concurrent with synthetic service load"]
    exercise["Exercise: Training versus inference/core resource<br/>contention. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput. Retain: E2,E4,E7,E8"]
    checks["Check: enforce reservations and approved admission;<br/>training cannot starve priority communication/inference"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-CORE,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-CORE,REQ-COM.

## TC-104

**What you test:** Retraining approval, reproducibility and regression gate.

**Setup:** `J/L/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Versioned offline training pipeline<br/>with failed/missing approval fixtures"]
    exercise["Exercise: Retraining approval, reproducibility and<br/>regression gate. Test boundary: Declared isolated AI<br/>pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion. Retain: E1,E8,E9"]
    checks["Check: reproduce approved evaluation within specified<br/>tolerance; no automatic production promotion after drift"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-GOV.

## TC-105

**What you test:** Distributed/federated training where implemented.

**Setup:** `C/J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock participant dropout, version<br/>mismatch and invalid update provenance"]
    exercise["Exercise: Distributed/federated training where<br/>implemented. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion; fault isolation, degraded state,<br/>restoration and rollback. Retain: E5,E8,E9"]
    checks["Check: validate participant/update eligibility, bounded<br/>convergence criterion and privacy/residency policy"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-GOV,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-GOV,REQ-RES.

## TC-106

**What you test:** AI/network-analytics feedback instability.

**Setup:** bounded-control `J/M=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: SIL policy loop with<br/>delayed/conflicting recommendations"]
    exercise["Exercise: AI/network-analytics feedback instability. Test<br/>boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: control<br/>permissions, scope/expiry, stability and stop precedence;<br/>session availability, loss, latency and throughput; AI<br/>quality, abstention, calibration, numerical validity and<br/>latency. Retain: E2,E4,E7,E8,E9"]
    checks["Check: meet approved stability/change-rate bounds;<br/>independent policy rejects unsafe oscillation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S5. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CTL,A-COM,A-AI. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CTL,REQ-COM,REQ-AI.

## TC-107

**What you test:** Advisory-only AI and revoked write authority.

**Setup:** `J/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock out-of-scope/expired network-<br/>control requests"]
    exercise["Exercise: Advisory-only AI and revoked write authority.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: control<br/>permissions, scope/expiry, stability and stop precedence;<br/>identity/tenant binding, track lineage and access<br/>decisions; authorization, interlocks, stop deadlines and<br/>safe state. Retain: E5,E6,E8,E9"]
    checks["Check: deny unauthorized writes independently of AI; no<br/>real response/engagement interface"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S5,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CTL,A-ID,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CTL,REQ-ID,REQ-SAF.

## TC-108

**What you test:** Decision provenance and operator interpretation.

**Setup:** `J/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Recorded predictions with<br/>missing/conflicting explanation metadata"]
    exercise["Exercise: Decision provenance and operator interpretation.<br/>Test boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>alarm delivery, acknowledgement, decisions and operator<br/>workload; freshness, ordering, validation, access and<br/>audit completeness. Retain: E1,E6,E8,E9"]
    checks["Check: show model/version, age, uncertainty and evidence<br/>limits; no fabricated rationale"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-HUM,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E6: operator actions, mock calls, interlocks and stops; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-HUM,REQ-DAT.

## TC-109

**What you test:** Track/object/device identity correlation.

**Setup:** `J/P/X/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic ID rotation, overlapping<br/>tracks, duplicate claims and UE changes"]
    exercise["Exercise: Track/object/device identity correlation. Test<br/>boundary: Declared isolated AI pipeline and runtime"]
    capture["Measure against approved truth / fixtures: identity/tenant<br/>binding, track lineage and access decisions; track<br/>continuity, identity swaps, age and reacquisition time;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E5,E7,E8"]
    checks["Check: preserve uncertain associations and separate<br/>subscriber, claimed identity and physical track"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-ID,A-TRK,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-ID,REQ-SEN,REQ-UNC.

## TC-110

**What you test:** Optional generative assistant handling untrusted reports.

**Setup:** applicable `J/H`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Benign test reports containing<br/>conflicting instructions and unsupported assertions"]
    exercise["Exercise: Optional generative assistant handling untrusted<br/>reports. Test boundary: Declared isolated AI pipeline and<br/>runtime"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; alarm<br/>delivery, acknowledgement, decisions and operator<br/>workload; control permissions, scope/expiry, stability and<br/>stop precedence. Retain: E5,E6,E8,E9"]
    checks["Check: treat reports as data, enforce independent<br/>permissions and never invent identification or response<br/>authority"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-HUM,A-CTL. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-HUM,REQ-CTL.

## TC-111

**What you test:** AI telemetry/drift monitor/evaluation service unavailable.

**Setup:** `C/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Disable isolated monitoring endpoint<br/>or hold evaluation results"]
    exercise["Exercise: AI telemetry/drift monitor/evaluation service<br/>unavailable. Test boundary: Declared isolated AI pipeline<br/>and runtime"]
    capture["Measure against approved truth / fixtures: AI quality,<br/>abstention, calibration, numerical validity and latency;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E4,E8,E9"]
    checks["Check: monitoring gap visible and approved continued-<br/>use/stop policy enforced; no assumed healthy quality"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-AI,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-AI,REQ-RES.

## TC-112

**What you test:** AI-domain shutdown, independent stop and qualified fallback.

**Setup:** `C/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated AI outage/stop with only<br/>approved fallback paths enabled"]
    exercise["Exercise: AI-domain shutdown, independent stop and<br/>qualified fallback. Test boundary: Declared isolated AI<br/>pipeline and runtime"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state; fault<br/>isolation, degraded state, restoration and rollback;<br/>session availability, loss, latency and throughput;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E2,E4,E6,E8"]
    checks["Check: stop works without AI, preserve communication and<br/>report unavailable/degraded identification"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S5. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF,A-RES,A-COM,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S2,S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF,REQ-RES,REQ-COM,REQ-UNC.
