# ISAC modes and sensing-capable radio configurations: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

**KPI / PM events:** use each TC ID in the [case-focus table](../kpi-pm.md#case-specific-focus-checks), plus all measurement/event groups inherited from its acceptance profiles. Actual collector names and thresholds need approval; local event labels are not standardized counters.

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-013

**What you test:** Communication-centric scheduling.

**Setup:** `M1/D/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved synthetic communication and<br/>sensing demand"]
    exercise["Exercise: Communication-centric scheduling. Test boundary:<br/>Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput. Retain: E1,E2"]
    checks["Check: quantify sensing degradation while preserving<br/>service budget"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs.

**Stop plan:** S1,S2; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM.

## TC-014

**What you test:** Sensing-centric scheduling.

**Setup:** `M2/D/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated configured resource-policy<br/>change"]
    exercise["Exercise: Sensing-centric scheduling. Test boundary:<br/>Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput. Retain: E1,E2"]
    checks["Check: sensing priority never silently overrides mandatory<br/>service limits"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs.

**Stop plan:** S1,S2; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM.

## TC-015

**What you test:** Joint operation.

**Setup:** `M3/D/W/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Concurrent/alternating bounded<br/>synthetic workloads under supported resource policies"]
    exercise["Exercise: Joint operation. Test boundary: Isolated radio<br/>and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput. Retain:<br/>E1,E2,E4"]
    checks["Check: simultaneous bounds hold, not just separate<br/>unloaded benchmarks"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S2; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM.

## TC-016

**What you test:** Sensing inhibition/fallback.

**Setup:** `M4/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Disable sensing through approved<br/>isolated control"]
    exercise["Exercise: Sensing inhibition/fallback. Test boundary:<br/>Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: session<br/>availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E2,E4,E6"]
    checks["Check: unavailable state visible; no fresh-looking sensing<br/>output"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-COM,A-RES,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-COM,REQ-RES,REQ-UNC.

## TC-017

**What you test:** Every supported mode transition.

**Setup:** `M/L=ALL` directed transitions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Exercise approved transition graph in<br/>SIL/HIL"]
    exercise["Exercise: Every supported mode transition. Test boundary:<br/>Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>session availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E2,E4"]
    checks["Check: account for transients, invalid observations and<br/>rollback"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-RES.

## TC-018

**What you test:** Monostatic radio health.

**Setup:** applicable `G/R/D`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Conducted/shielded emulator varying<br/>approved leakage/residual model"]
    exercise["Exercise: Monostatic radio health. Test boundary: Isolated<br/>radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; calibration<br/>residuals, clock drift and equipment health. Retain: E1,E3"]
    checks["Check: radio-validity limits enforced and observations<br/>invalidated when exceeded"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-RAD. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-RAD.

## TC-019

**What you test:** Bistatic alignment.

**Setup:** applicable `G/N`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated timing/geometry metadata<br/>perturbation"]
    exercise["Exercise: Bistatic alignment. Test boundary: Isolated<br/>radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; calibration<br/>residuals, clock drift and equipment health; freshness,<br/>ordering, validation, access and audit completeness.<br/>Retain: E1,E3,E5"]
    checks["Check: detect invalid alignment and suppress misleading<br/>estimates"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-RAD,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E5: input provenance, validation, access and integrity.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-RAD,REQ-DAT.

## TC-020

**What you test:** Multistatic node loss/disagreement.

**Setup:** applicable `G/N`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Drop or delay synthetic node<br/>observations"]
    exercise["Exercise: Multistatic node loss/disagreement. Test<br/>boundary: Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E1,E3,E4"]
    checks["Check: degraded coverage/uncertainty reflects surviving<br/>valid nodes"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-RES.

## TC-021

**What you test:** Passive illumination unavailable.

**Setup:** passive `G/R`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Remove modeled illuminator from<br/>replay"]
    exercise["Exercise: Passive illumination unavailable. Test boundary:<br/>Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3,E4"]
    checks["Check: absence of illumination is not reported as absence<br/>of objects"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-022

**What you test:** External radar/passive/SDR interface compatibility.

**Setup:** `R/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Golden and invalid sample/interface<br/>fixtures in isolation"]
    exercise["Exercise: External radar/passive/SDR interface<br/>compatibility. Test boundary: Isolated radio and resource<br/>controls"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; freshness,<br/>ordering, validation, access and audit completeness.<br/>Retain: E1,E3,E5"]
    checks["Check: units, frames, calibration and validity preserve<br/>their meaning"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E5: input provenance, validation, access and integrity.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-DAT.

## TC-023

**What you test:** Duplex/carrier/band/beam/illumination changes.

**Setup:** `D/W=ALL` supported edges. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved reconfiguration in<br/>shielded/conducted HIL"]
    exercise["Exercise: Duplex/carrier/band/beam/illumination changes.<br/>Test boundary: Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput; calibration<br/>residuals, clock drift and equipment health. Retain:<br/>E1,E2,E3"]
    checks["Check: independently qualify each configuration and<br/>transition, including observation gaps"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM,A-RAD. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health.

**Stop plan:** S1,S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-RAD.

## TC-024

**What you test:** UE state and network architecture dependencies.

**Setup:** `N/U=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated UE/core state emulator and<br/>test sessions"]
    exercise["Exercise: UE state and network architecture dependencies.<br/>Test boundary: Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E2,E4"]
    checks["Check: expose actual dependency, including unsupported/UE-<br/>absent conditions"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-RES.

## TC-025

**What you test:** Calibration drift or invalid calibration.

**Setup:** `R/D/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Perturb calibration metadata in<br/>simulator"]
    exercise["Exercise: Calibration drift or invalid calibration. Test<br/>boundary: Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3,E4"]
    checks["Check: detect invalidity, withhold confidence and require<br/>approved recalibration"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-UNC.

## TC-026

**What you test:** Timing source drift/loss.

**Setup:** `G/N/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Clock fault through an isolated<br/>emulator, never over-air spoofing"]
    exercise["Exercise: Timing source drift/loss. Test boundary:<br/>Isolated radio and resource controls"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; track<br/>continuity, identity swaps, age and reacquisition time;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E1,E3,E4"]
    checks["Check: identify dependent invalid observations and bounded<br/>recovery"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-TRK,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-SEN,REQ-RES.
