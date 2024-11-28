from datetime import datetime

from db.models.device import Device
from db.models.interaction import Interaction


def extract_normalized_devices(raw_data):
    raw_devices = raw_data["devices"]
    normalized_devices = [normalize_device(raw_device) for raw_device in raw_devices]
    return normalized_devices

def normalize_device(raw_device):
    device = Device(
        id=raw_device['id'],
        brand=raw_device['brand'],
        model=raw_device['model'],
        os=raw_device['os'],
        latitude=raw_device['location']['latitude'],
        longitude=raw_device['location']['longitude'],
        altitude_meters=raw_device['location']['altitude_meters'],
        accuracy_meters=raw_device['location']['accuracy_meters']
    )
    return device

def normalize_interaction(interaction_data):
    interaction = Interaction(
        from_device=interaction_data['from_device'],
        to_device=interaction_data['to_device'],
        method=interaction_data['method'],
        bluetooth_version=interaction_data['bluetooth_version'],
        signal_strength_dbm=interaction_data['signal_strength_dbm'],
        distance_meters=interaction_data['distance_meters'],
        duration_seconds=interaction_data['duration_seconds'],
        timestamp=datetime.fromisoformat(interaction_data['timestamp'])
    )
    return interaction



def extract_normalized_interaction(raw_data):
    raw_interaction = raw_data["interaction"]
    normalized_interaction = normalize_interaction(raw_interaction)
    return normalized_interaction

