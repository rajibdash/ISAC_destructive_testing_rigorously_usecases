# Selected compound failures and restoration: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-051

**What you test:** Degraded scene plus peak communication demand.

**Setup:** `V/Q/M=ALL` applicable. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Replay scene plus isolated traffic<br/>generator"]
    exercise["Exercise: Degraded scene plus peak communication demand.<br/>Test boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E2,E4"]
    checks["Check: report sensing degradation without sacrificing<br/>approved service budget"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-UNC.

## TC-052

**What you test:** Timing loss plus multistatic-node loss.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Combined isolated clock/node emulator<br/>faults"]
    exercise["Exercise: Timing loss plus multistatic-node loss. Test<br/>boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; track<br/>continuity, identity swaps, age and reacquisition time;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E1,E3,E4"]
    checks["Check: no falsely precise fused result or premature<br/>recovery"]
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

## TC-053

**What you test:** Compute pressure plus stale-data backlog.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded load and replay delay"]
    exercise["Exercise: Compute pressure plus stale-data backlog. Test<br/>boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>freshness, ordering, validation, access and audit<br/>completeness; fault isolation, degraded state, restoration<br/>and rollback. Retain: E1,E4,E5"]
    checks["Check: shed stale work and visibly mark lost timeliness"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity.

**Stop plan:** S1,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-DAT,REQ-RES.

## TC-054

**What you test:** Sensor disagreement plus unavailable operator notification.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Conflicting replay and mock<br/>notification outage"]
    exercise["Exercise: Sensor disagreement plus unavailable operator<br/>notification. Test boundary: Isolated multi-component<br/>system"]
    capture["Measure against approved truth / fixtures:<br/>unknown/ambiguous decisions and confidence calibration;<br/>alarm delivery, acknowledgement, decisions and operator<br/>workload; authorization, interlocks, stop deadlines and<br/>safe state. Retain: E1,E4,E6"]
    checks["Check: retain uncertainty and inhibit mocked action<br/>without authorization"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-UNC,A-HUM,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-UNC,REQ-HUM,REQ-SAF.

## TC-055

**What you test:** Shared power/timing/backhaul dependency loss.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Common-cause model in SIL/HIL, no<br/>live infrastructure disruption"]
    exercise["Exercise: Shared power/timing/backhaul dependency loss.<br/>Test boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: session<br/>availability, loss, latency and throughput; calibration<br/>residuals, clock drift and equipment health; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E2,E3,E4"]
    checks["Check: expose correlated loss rather than assume<br/>independent redundancy"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-COM,A-RAD,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-COM,REQ-RAD,REQ-RES.

## TC-056

**What you test:** Restart plus stale model/configuration state.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated restart with version-<br/>mismatched fixtures"]
    exercise["Exercise: Restart plus stale model/configuration state.<br/>Test boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E4,E5"]
    checks["Check: reject incompatible state before declaring<br/>readiness"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-RES.

## TC-057

**What you test:** Redundancy failover plus evidence-store outage.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated partition and quota-limited<br/>evidence service"]
    exercise["Exercise: Redundancy failover plus evidence-store outage.<br/>Test boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E4,E5,E6"]
    checks["Check: make missing evidence and authority ownership<br/>explicit"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S5. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-RES.

## TC-058

**What you test:** Stop request during mode change/recovery.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock stop while isolated transition<br/>is in progress"]
    exercise["Exercise: Stop request during mode change/recovery. Test<br/>boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: authorization,<br/>interlocks, stop deadlines and safe state; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E2,E4,E6"]
    checks["Check: stop takes precedence and recovery cannot re-enable<br/>inhibited outputs"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S5. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SAF,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S2,S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SAF,REQ-RES.

## TC-059

**What you test:** Recovery after compound degraded operation.

**Setup:** `L/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Remove emulated faults in controlled<br/>order"]
    exercise["Exercise: Recovery after compound degraded operation. Test<br/>boundary: Isolated multi-component system"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; session<br/>availability, loss, latency and throughput; calibration<br/>residuals, clock drift and equipment health; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E2,E3,E4"]
    checks["Check: recalibrate/revalidate dependencies before<br/>declaring restored service"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-COM,A-RAD,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-RAD,REQ-RES.

## TC-060

**What you test:** Repeated fault/recovery cycles and sustained observation.

**Setup:** Use the applicable declared configuration and reviewed scenario conditions. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved-duration synthetic endurance<br/>run"]
    exercise["Exercise: Repeated fault/recovery cycles and sustained<br/>observation. Test boundary: Isolated multi-component<br/>system"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>session availability, loss, latency and throughput;<br/>freshness, ordering, validation, access and audit<br/>completeness; fault isolation, degraded state, restoration<br/>and rollback. Retain: E1,E2,E4,E5"]
    checks["Check: bound resource growth, state drift and recurring<br/>failures"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-COM,A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity.

**Stop plan:** S1,S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-DAT,REQ-RES.
