import asyncio
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from traveltimepy import Coordinates, Cycling, TravelTimeSdk


def get_api():
    app_id = os.environ.get("APPID")
    api_key = os.environ.get("APIKEY")
    if app_id and api_key:
        return TravelTimeSdk(app_id=app_id, api_key=api_key)
    else:
        raise ValueError("app id or api key are None")


async def get_iso(api, coords, travel_time, arrival_time, mode):
    isochrone = await api.time_map_geojson_async(
        coordinates=coords,
        transportation=mode,
        travel_time=travel_time,
        arrival_time=arrival_time,
    )
    return isochrone


# def make_list(isochrone: TimeMapResults):
#     print(dir(isochrone))


def save_to_file(data, fname):
    with open(fname, "w") as fout:
        fout.write(data.json())


def save_iso(coords, travel_time, arrival_time, mode, fname):
    # snap_penalty: SnapPenalty - When enabled, walking time and distance from the departure location to the nearest road, and from the nearest road to the arrival location, are added to the total travel time and distance of a journey. Enabled by default.

    api = get_api()
    res = asyncio.run(
        get_iso(
            api=api,
            coords=coords,
            travel_time=travel_time,
            arrival_time=arrival_time,
            mode=mode,
        ),
    )
    save_to_file(res, fname)


def get_park():
    coord_park = Coordinates(lat=40.75197891634803, lng=-73.97837700147562)
    travel_time = 2160  # 36min in seconds
    arrival_time = datetime(2024, 9, 2, 10, 00, tzinfo=ZoneInfo("America/New_York"))

    save_iso(
        coords=[coord_park],
        travel_time=travel_time,
        arrival_time=arrival_time,
        mode=Cycling(),
        fname="park120cycle.json",
    )


def get_costco():
    coord_astoria = Coordinates(lat=40.767534384124986, lng=-73.93911284709553)
    # coord_astoria = Coordinates(lat=40.73360059919057, lng=-73.86310863162494)
    travel_time = 1200  # 20min in seconds
    arrival_time = datetime(2024, 9, 7, 19, 00, tzinfo=ZoneInfo("America/New_York"))

    save_iso(
        coords=[coord_astoria],
        travel_time=travel_time,
        arrival_time=arrival_time,
        mode=Cycling(),
        fname="costcocycle.json",
    )


def get_aldis():
    coord_queens = Coordinates(lat=40.73360059919057, lng=-73.86310863162494)
    coord_ues = Coordinates(lat=40.79574957012375, lng=-73.93177459994466)
    travel_time = 1200  # 20min in seconds
    arrival_time = datetime(2024, 9, 7, 19, 00, tzinfo=ZoneInfo("America/New_York"))

    save_iso(
        coords=[coord_queens, coord_ues],
        travel_time=travel_time,
        arrival_time=arrival_time,
        mode=Cycling(),
        fname="aldicycle.json",
    )


def get_bouldering():
    coord_bb = Coordinates(lat=40.753075372773836, lng=-73.9398691457113)
    coord_vital = Coordinates(lat=40.72283538709986, lng=-73.95474935983061)
    travel_time = 720  # 12min in seconds
    arrival_time = datetime(2024, 9, 7, 10, 00, tzinfo=ZoneInfo("America/New_York"))

    save_iso(
        coords=[coord_bb, coord_vital],
        travel_time=travel_time,
        arrival_time=arrival_time,
        mode=Cycling(),
        fname="bouldercycle.json",
    )
