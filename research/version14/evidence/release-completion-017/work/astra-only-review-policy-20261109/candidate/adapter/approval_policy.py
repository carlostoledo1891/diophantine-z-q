"""Required approval policy, applied only to authenticated run observations.

This records controller/operator provenance, not provider-signed serving metadata.
Historical events and contributions remain admissible ledger records.
"""
PUBLIC_REPOSITORY_ID = 1446122118
REQUIRED_MODEL = 'gpt-6-astra'

def approval_allowed(repository_id, model, reviewer_type='model'):
    return repository_id != PUBLIC_REPOSITORY_ID or (
        reviewer_type == 'model' and model == REQUIRED_MODEL)
