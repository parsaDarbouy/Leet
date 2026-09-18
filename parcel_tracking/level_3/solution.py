class ParcelTrackingSystem:
    def register_parcel(self, parcel_id: str) -> bool:
        raise NotImplementedError

    def add_event(self, parcel_id: str, event: str) -> bool:
        raise NotImplementedError

    def get_event_count(self, parcel_id: str) -> int:
        raise NotImplementedError

    def get_events(self, parcel_id: str) -> list[str] | None:
        raise NotImplementedError

    def get_top_parcels(self, k: int) -> list[str]:
        raise NotImplementedError

    def assign_courier(self, parcel_id: str, courier_id: str) -> bool:
        raise NotImplementedError

    def get_courier(self, parcel_id: str) -> str | None:
        raise NotImplementedError

    def get_courier_parcels(self, courier_id: str) -> list[str]:
        raise NotImplementedError

    def add_courier_event(self, courier_id: str, event: str) -> bool:
        raise NotImplementedError

    def get_courier_event_count(self, courier_id: str) -> int:
        raise NotImplementedError
