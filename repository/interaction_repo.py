from returns.maybe import Maybe

from db.database import driver
from db.models.interaction import Interaction


def create_call_relationship(interaction: Interaction):
    with driver.session() as session:
        query = """
            MATCH (d1:Device {id: $device_id_1})
            MATCH (d2:Device {id: $device_id_2})
            WITH d1, d2 LIMIT 1
            MERGE (d1)-[r:CALL]->(d2)
            ON CREATE SET r.method = $method,
                          r.bluetooth_version = $bluetooth_version,
                          r.signal_strength_dbm = $signal_strength_dbm,
                          r.distance_meters = $distance_meters,
                          r.duration_seconds = $duration_seconds,
                          r.timestamp = $timestamp
            RETURN r
            """

        params = {
            "device_id_1": interaction.from_device,
            "device_id_2": interaction.to_device,
            "method": interaction.method,
            "bluetooth_version": interaction.bluetooth_version,
            "signal_strength_dbm": interaction.signal_strength_dbm,
            "distance_meters": interaction.distance_meters,
            "duration_seconds": interaction.duration_seconds,
            "timestamp": str(interaction.timestamp)
        }

        res = session.run(query, params).data()

        return Maybe.from_optional(res)
