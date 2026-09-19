class Parcel:
    def __init__(self, parcel_id: str):
        self.parcel_id = parcel_id
        self.events = []
        self.courier = None

class ParcelTrackingSystem:
    def __init__(self):
        self.parcels = {}
        self.courier_event = {}

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

    def get_top_parcels(self, k: int) -> list[str]:
        if k <= 0:
            return []
        keys = list(self.parcels.keys())
        keys.sort(key= lambda parcel_id: (-len(self.parcels[parcel_id].events), parcel_id))
        return keys[:k]

    def assign_courier(self, parcel_id: str, courier_id: str) -> bool:
        if parcel_id in self.parcels:
            self.parcels[parcel_id].courier = courier_id
            return True
        return False

    def get_courier(self, parcel_id: str) -> str | None:
        if parcel_id in self.parcels:
            return self.parcels[parcel_id].courier
        return None

    def get_courier_parcels(self, courier_id: str) -> list[str]:
        parcels = []
        parcels_list = list(self.parcels.keys())
        for parcel_id in parcels_list:
            if courier_id == self.parcels[parcel_id].courier:
                parcels.append(parcel_id)
        parcels.sort()
        return parcels

    def add_courier_event(self, courier_id: str, event: str) -> bool:
        if courier_id in self.courier_event:
            self.courier_event[courier_id].append(event)
            return True
        self.courier_event[courier_id] = [event]
        return True

    def get_courier_event_count(self, courier_id: str) -> int:
        if courier_id in self.courier_event:
            return len(self.courier_event[courier_id])
        for parcel in self.parcels.values():
            if parcel.courier == courier_id:
                return 0
        return -1
