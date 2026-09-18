class Parcel:
    def __init__(self, parcel_id: str):
        self.parcel_id = parcel_id
        self.events = []

class ParcelTrackingSystem:
    def __init__(self):
        self.parcels = {}
    def register_parcel(self, parcel_id: str) -> bool:
        if parcel_id in self.parcels:
            return False
        self.parcels[parcel_id] = Parcel(parcel_id)
        return True

    def add_event(self, parcel_id: str, event: str) -> bool:
        if parcel_id in self.parcels:
            self.parcels[parcel_id].events.append(event)
            return True
        return False

    def get_event_count(self, parcel_id: str) -> int:
        if parcel_id not in self.parcels:
            return -1
        return len(self.parcels[parcel_id].events)

    def get_events(self, parcel_id: str) -> list[str] | None:
        if parcel_id in self.parcels:
            return list(self.parcels[parcel_id].events)
        return None

