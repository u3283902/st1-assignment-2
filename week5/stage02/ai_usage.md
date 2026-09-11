
# AI Requirements Review (Part F)
**Tool used:** Microsoft Copilot (UC-approved GenAI tool)

**Prompt used:** "Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation."

## Scope
| Area | Issue Raised | Evidence-based? |
|---|---|---|
| Patient details | "Name" given as example in scope, but FR-01 doesn't define required fields | Yes |
| Finding records | Scope says "find patient records," FR-02 only supports search by name | Yes |
| Update vs. cancel/reschedule | FR-08 says "update," scope separately lists cancel/reschedule — unclear if these are the same action | Yes |
| Conflict rules | Scope doesn't specify how cancelled appointments affect conflict checks (relevant to FR-09) | Yes |
| Provisional items | Recurring appointments and cancellation permissions remain unconfirmed | Yes |

## Functional Requirements
| FR | Issue Raised | Evidence-based? |
|---|---|---|
| FR-01 | "Patient details" undefined (which fields required) | Yes |
| FR-02 | Case sensitivity, partial matches, duplicate names not addressed | Yes |
| FR-03 | Time format and practitioner fields not defined; overlaps for different practitioners not addressed | Yes |
| FR-04 | "Same time" ambiguous — exact timestamp vs. time range | Yes |
| FR-06 | "Past" appointments ambiguous, especially for cancelled future ones | Yes |
| FR-07 | Allowed status values not defined | Yes |
| FR-08 | Which fields can be updated not specified | Yes |
| FR-09 | Possible inconsistency with FR-04 — does cancelling remove conflict-check relevance? | Yes |

## Non-Functional Requirements
| NFR | Issue Raised | Evidence-based? |
|---|---|---|
| NFR-01 | "Missing" field ambiguous (null vs. empty string vs. whitespace) | Yes |
| NFR-02 | "Extensive" training is subjective, not measurable | Yes |
| NFR-03 | "Separate" is vague — could mean modular code, UI separation, or microservices | Yes |
| NFR-04 | "Normal operation" undefined (e.g. does this cover power/network failure?) | Yes |

## User Stories
| Story | Issue Raised | Evidence-based? |
|---|---|---|
| 1 (Booking) | Error message content/wording not defined | Yes |
| 2 (Search) | Same ambiguities as FR-02 (case sensitivity, partial match) | Yes |
| 3 (Cancel) | Reinstating a cancelled appointment not addressed | Yes |
| 4 (Practitioner conflicts) | Notification/visibility expectations for practitioners not defined | Yes |

# Verify AI Review (Part G)
## Scope
| **Area** | **Issue Raised** | **Valid Evidence?** | **Status** |
| ----- | ----- | ----- | ----- |
| Patient Details | "Name" undefined | Yes, genuine gap | Accepted |
| Finding Records | "Find records" differs from search by name | Yes, genuine gap | Accepted |
| Update VS Cancel/Reschedule | Unclear if "Update" and "Cancel"/"Reschedule" are the same function | Yes, genuine gap | Modified |
| Conflict Rules | Scope doesn't specify how cancelled appointments affect conflict checks | Yes, valid issue | Accepted |
| Provisional Items | Recurring appointments and cancellation permissions unconfirmed, but not verified by client | Yes, genuine gap | Unverified |

## Functional Requirements
| **FR** | **Issue Raised** | **Valid Evidence?** | **Status** |
| ----- | ----- | ----- | ----- |
| FR-01 | Undefined fields for "Patient Details" | Yes, valid gap | Accepted |
| FR-02 | Case sensitivity, partial matches, and duplicate names not addressed | Yes, valid gap | Accepted |
| FR-03 | Time format and practitioner fields not defined | Yes, genuine gap | Accepted |
| FR-04 | "Same time" is broad | Yes, valid point | Accepted |
| FR-06 | "Past appointments" is broad | Valid point, but timeframe is not defined by client | Modified |
| FR-07 | Allowed status values not defined | Yes, valid gap | Accepted |
| FR-08 | Unclear which fields can be updated | Yes, valid gap | Accepted |
| FR-09 | Possible inconsistency with FR-04 | Yes, valid gap | Accepted |

## Non-Functional Requirements
| **NFR** | **Issue Raised** | **Valid Evidence?** | **Status** |
| ----- | ----- | ----- | ----- |
| NFR-01 | "Missing" field is broad | Yes, valid gap | Accepted |
| NFR-02 | "Extensive" training is subjective | Yes, valid gap | Accepted |
| NFR-03 | "Separate" is broad | Overreach for a small prototype | Rejected |
| NFR-04 | "Normal operation" is not defined | Overreach for a small prototype | Rejected |

## User Stories
| **Story Number** | **Issue Raised** | **Valid Evidence?** | **Status** |
| ----- | ----- | ----- | ----- |
| 1 | Error message not defined | Implementation detail | Rejected |
| 2 | Case sensitive and partial match not addressed | Yes, valid gap | Accepted |
| 3 | Reinstating a cancelled appointment not addressed | Valid gap, but unaddressed by client | Unverified |
| 4 | Visibility for practitioners not addressed | Invents new feature not outlined by client | Rejected |

**Note:** the original FR-07 isn't included in the Functional Requirements anymore as it was merged with FR-08 as per the AI review to better define the "update" function.