import toolz as t
from returns.maybe import Maybe
from db.database import driver
from db.models.device import Device


def get_all_devices():
    with driver.session() as session:
        query = """
        MATCH (d:Device) RETURN d
        """
        res = session.run(query).data()
        return t.pipe(
            res,
            t.partial(t.pluck, "d"),
            list
        )

def get_device_by_method(method: str):
    with driver.session() as session:
        query = """
        MATCH p = (d1:Device)-[rel:CALL*]->(d2:Device)
        WHERE all(r IN relationships(p) WHERE r.method = $method)
        RETURN p AS path, length(p) AS path_length
        """

        params = {
            "method": method
        }

        res = session.run(query, params).data()

        return Maybe.from_optional(res)

def get_device_with_better_connection(signal_strength: float):
    with driver.session() as session:
        query = """
        MATCH (d1:Device)-[rel:CALL]->(d2:Device)
        WHERE rel.signal_strength_dbm > $signal_strength
        RETURN d1, d2
        """

        params = {
            "signal_strength": signal_strength
        }

        res = session.run(query, params).data()

        return Maybe.from_optional(res)



def insert_device(device: Device):
    with driver.session() as session:
        query = """
        MERGE (d:Device {
            id: $id,
            brand: $brand,
            model: $model,
            os: $os,
            latitude: $latitude,
            longitude: $longitude,
            altitude_meters: $altitude_meters,
            accuracy_meters: $accuracy_meters
        }) RETURN d
        """

        params = {
            "id": device.id,
            "brand": device.brand,
            "model": device.model,
            "os": device.os,
            "latitude": device.latitude,
            "longitude": device.longitude,
            "altitude_meters": device.altitude_meters,
            "accuracy_meters": device.accuracy_meters
        }

        res = session.run(query, params).single()

        return (Maybe.from_optional(res.get("d"))
                .map(lambda d: dict(d)))


def delete_device(device_id: str):
    with driver.session() as session:
        query = """
        MATCH (d:Device {
            id: $id
        }) DETACH DELETE d
        """

        params = {
            "id": device_id
        }

        session.run(query, params)
        return {"success": True, "message": "Device deleted successfully"}



