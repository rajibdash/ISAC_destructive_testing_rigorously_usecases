# Data, service, and infrastructure fault injection: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-027

**What you test:** Stale/reordered/duplicate observations.

**Setup:** `X/N/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Replay transport faults at isolated<br/>interfaces"]
    exercise["Exercise: Stale/reordered/duplicate observations. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; track<br/>continuity, identity swaps, age and reacquisition time.<br/>Retain: E1,E4,E5"]
    checks["Check: age/order rules enforced with visible rejection or<br/>quarantine"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-SEN.

## TC-028

**What you test:** Invalid schema, units or reference frame.

**Setup:** `R/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded invalid fixtures in test-only<br/>input adapter"]
    exercise["Exercise: Invalid schema, units or reference frame. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E5"]
    checks["Check: reject/quarantine visibly; no silently plausible<br/>converted track"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E5: input provenance, validation, access and integrity.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-UNC.

## TC-029

**What you test:** Missing/untrusted input provenance.

**Setup:** `X/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic unauthorized/stale-<br/>credential requests"]
    exercise["Exercise: Missing/untrusted input provenance. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness;<br/>authorization, interlocks, stop deadlines and safe state.<br/>Retain: E5,E6"]
    checks["Check: deny unauthorized inputs/actions with attributable<br/>audit evidence"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-SAF.

## TC-030

**What you test:** Sensor disconnection or RF-chain health loss.

**Setup:** `R/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: HIL health signal or replay-stream<br/>disconnect"]
    exercise["Exercise: Sensor disconnection or RF-chain health loss.<br/>Test boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; fault<br/>isolation, degraded state, restoration and rollback;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3,E4"]
    checks["Check: detect outage and stop presenting stale data as<br/>healthy"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-RES,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-RES,REQ-UNC.

## TC-031

**What you test:** Compute/accelerator pressure.

**Setup:** `M/Q/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded synthetic load in isolated<br/>compute"]
    exercise["Exercise: Compute/accelerator pressure. Test boundary:<br/>Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>session availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E2,E4"]
    checks["Check: load shedding preserves declared service and<br/>observation-age rules"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-COM,REQ-RES.

## TC-032

**What you test:** Queue/storage pressure and evidence loss.

**Setup:** `Q/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Quota-limited test storage and<br/>bounded queue load"]
    exercise["Exercise: Queue/storage pressure and evidence loss. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E4,E5,E6"]
    checks["Check: evidence loss visible; no success claim when<br/>required evidence is absent"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-RES.

## TC-033

**What you test:** Backhaul delay, loss or disconnection.

**Setup:** `N/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated network emulator"]
    exercise["Exercise: Backhaul delay, loss or disconnection. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>session availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E2,E4"]
    checks["Check: bounded local operation and visible loss of<br/>external dependencies"]
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

## TC-034

**What you test:** Core/control-service unavailable.

**Setup:** `N/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Stop isolated mock service"]
    exercise["Exercise: Core/control-service unavailable. Test boundary:<br/>Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: session<br/>availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E2,E4,E6"]
    checks["Check: expose unavailable functions without unsafe retry<br/>storms"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-COM,REQ-RES.

## TC-035

**What you test:** Power-state transition or restart.

**Setup:** `R/N/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved power-state HIL model or<br/>software restart"]
    exercise["Exercise: Power-state transition or restart. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: session<br/>availability, loss, latency and throughput; calibration<br/>residuals, clock drift and equipment health; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E2,E3,E4"]
    checks["Check: no physical mains manipulation; validate readiness<br/>before healthy state"]
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

## TC-036

**What you test:** Thermal warning/derating.

**Setup:** `R/Q/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Simulated health input; do not<br/>overheat equipment"]
    exercise["Exercise: Thermal warning/derating. Test boundary:<br/>Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; session<br/>availability, loss, latency and throughput; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E2,E3,E4"]
    checks["Check: derating and shutdown respect approved<br/>equipment/service policies"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-COM,REQ-RES.

## TC-037

**What you test:** Component crash and restart loop.

**Setup:** `N/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Controlled failure of isolated<br/>process/container"]
    exercise["Exercise: Component crash and restart loop. Test boundary:<br/>Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: fault<br/>isolation, degraded state, restoration and rollback; track<br/>continuity, identity swaps, age and reacquisition time;<br/>session availability, loss, latency and throughput.<br/>Retain: E1,E2,E4"]
    checks["Check: no stale-state resurrection or unbounded restart"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RES,A-TRK,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state.

**Stop plan:** S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RES,REQ-SEN,REQ-COM.

## TC-038

**What you test:** Model/configuration update and rollback.

**Setup:** `M/R/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Versioned approved test update,<br/>including incompatible fixture"]
    exercise["Exercise: Model/configuration update and rollback. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: detections,<br/>misses, false alarms, position/velocity error; freshness,<br/>ordering, validation, access and audit completeness; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E1,E4,E5"]
    checks["Check: reject incompatibility, retain provenance and<br/>restore qualified version"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-SEN,A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-DAT,REQ-RES.

## TC-039

**What you test:** Redundant-node failover and split view.

**Setup:** `N/G=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated partition/failover emulator"]
    exercise["Exercise: Redundant-node failover and split view. Test<br/>boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: track<br/>continuity, identity swaps, age and reacquisition time;<br/>freshness, ordering, validation, access and audit<br/>completeness; fault isolation, degraded state, restoration<br/>and rollback. Retain: E1,E4,E5"]
    checks["Check: avoid duplicate authoritative decisions and<br/>reconcile explicitly"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S5. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-TRK,A-DAT,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity.

**Stop plan:** S3,S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-SEN,REQ-DAT,REQ-RES.

## TC-040

**What you test:** Alarm delivery/acknowledgement path failure.

**Setup:** `N/L/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Disable mock notification endpoint"]
    exercise["Exercise: Alarm delivery/acknowledgement path failure.<br/>Test boundary: Isolated data and service dependencies"]
    capture["Measure against approved truth / fixtures: alarm delivery,<br/>acknowledgement, decisions and operator workload; fault<br/>isolation, degraded state, restoration and rollback.<br/>Retain: E4,E6"]
    checks["Check: unavailable delivery and escalation visible; no<br/>false acknowledgement"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-HUM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops.

**Stop plan:** S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-HUM,REQ-RES.
