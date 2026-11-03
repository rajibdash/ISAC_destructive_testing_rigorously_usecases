# Sensing, identity, and environmental conditions: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-001

**What you test:** Reference scene.

**Setup:** `M/G/R/D=ALL` supported sensing configurations. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Qualified synthetic/reference replay,<br/>then authorized benign confirmation where permitted"]
    exercise["Exercise: Reference scene. Test boundary: Sensing and<br/>fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput; calibration<br/>residuals, clock drift and equipment health. Retain:<br/>E1,E2,E3"]
    checks["Check: meet baseline bounds and declare valid sensing<br/>envelope"]
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

## TC-002

**What you test:** No-object scene and false alarms.

**Setup:** `V/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Empty-scene recordings with labeled<br/>clutter"]
    exercise["Exercise: No-object scene and false alarms. Test boundary:<br/>Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1"]
    checks["Check: false-alarm denominator defined; no invented<br/>object/hostility labels"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-003

**What you test:** Unidentified versus authorized object.

**Setup:** `P/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic metadata present, absent,<br/>ambiguous and conflicting"]
    exercise["Exercise: Unidentified versus authorized object. Test<br/>boundary: Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures:<br/>unknown/ambiguous decisions and confidence calibration;<br/>freshness, ordering, validation, access and audit<br/>completeness. Retain: E1,E5,E6"]
    checks["Check: unknown remains unknown and authorization remains a<br/>separate decision"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-UNC,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-UNC,REQ-DAT,REQ-SAF.

## TC-004

**What you test:** Benign confusers.

**Setup:** `V/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Labeled birds, aircraft and moving<br/>clutter in authorized datasets"]
    exercise["Exercise: Benign confusers. Test boundary: Sensing and<br/>fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1"]
    checks["Check: measure per-class confusion and retain ambiguous<br/>classifications"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-005

**What you test:** Visibility/propagation changes.

**Setup:** `V/R/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Qualified weather/lighting model or<br/>replay"]
    exercise["Exercise: Visibility/propagation changes. Test boundary:<br/>Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3"]
    checks["Check: report stratum-specific degradation and unsupported<br/>conditions"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-006

**What you test:** Occluded or unobservable object.

**Setup:** `G/U/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Scene replay with declared<br/>observation gaps"]
    exercise["Exercise: Occluded or unobservable object. Test boundary:<br/>Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E4"]
    checks["Check: declare unobservable/stale state rather than a<br/>confident extrapolation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-007

**What you test:** Multipath/duplicate observations.

**Setup:** `G/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Channel/scene simulator within<br/>approved models"]
    exercise["Exercise: Multipath/duplicate observations. Test boundary:<br/>Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; track<br/>continuity, identity swaps, age and reacquisition time.<br/>Retain: E1,E3"]
    checks["Check: quantify ghost/duplicate tracks and uncertainty"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-RAD.

## TC-008

**What you test:** Multiple objects and association ambiguity.

**Setup:** `G/X/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Labeled multi-object synthetic/replay<br/>scenes"]
    exercise["Exercise: Multiple objects and association ambiguity. Test<br/>boundary: Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E4"]
    checks["Check: bound association errors and expose unresolved<br/>identities"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-009

**What you test:** Observation gap and reacquisition.

**Setup:** `L/U=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Pause/resume a replay stream"]
    exercise["Exercise: Observation gap and reacquisition. Test<br/>boundary: Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time.<br/>Retain: E1,E4"]
    checks["Check: stale tracks expire and reacquisition does not<br/>silently inherit identity"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-RES.

## TC-010

**What you test:** Sensing/communication boundary mismatch.

**Setup:** `U/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Independent modeled communication and<br/>sensing availability"]
    exercise["Exercise: Sensing/communication boundary mismatch. Test<br/>boundary: Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E2,E4"]
    checks["Check: no sensing-coverage claim based only on<br/>communication coverage"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-UNC.

## TC-011

**What you test:** Cooperative versus noncooperative target model.

**Setup:** `P/G=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Metadata removal only in<br/>simulation/replay"]
    exercise["Exercise: Cooperative versus noncooperative target model.<br/>Test boundary: Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E5"]
    checks["Check: characterize dependency on cooperation without<br/>assuming live target cooperation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-UNC.

## TC-012

**What you test:** Sensor modality disagreement.

**Setup:** `X=ALL` fusion combinations. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Replay intentionally inconsistent but<br/>labeled sensor outputs"]
    exercise["Exercise: Sensor modality disagreement. Test boundary:<br/>Sensing and fusion pipeline"]
    capture["Measure against approved truth / fixtures:<br/>unknown/ambiguous decisions and confidence calibration;<br/>freshness, ordering, validation, access and audit<br/>completeness. Retain: E1,E5,E6"]
    checks["Check: conflict visible, provenance retained, no<br/>unsupported certainty"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-UNC,A-DAT. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-UNC,REQ-DAT.
