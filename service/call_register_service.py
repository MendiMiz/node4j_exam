from repository.device_repo import insert_device
from repository.interaction_repo import create_call_relationship
from service.data_normalization import extract_normalized_devices, extract_normalized_interaction
import toolz as t

def register_call(raw_call):

    if device_calling_himself(raw_call):
        return {"error": "the device is calling himself"}

    #insert devices after normalization
    inserted_devices =  t.pipe(
        raw_call,
        extract_normalized_devices,
        (lambda calls: [insert_device(call) for call in calls])
    )

    # insert call relation after normalization
    inserted_call_relation = t.pipe(
        raw_call,
        extract_normalized_interaction,
        create_call_relationship
        )

    return {"devices": inserted_devices, "call_rel": inserted_call_relation}

def device_calling_himself(raw_data):
    return raw_data["devices"][0]["id"] == raw_data["devices"][1]["id"]