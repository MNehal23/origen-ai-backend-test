# part_a/app/api/routers.py
from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional
from app.db.database import DATABASE_URL
import asyncpg
import json
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# @router.get("/machines", response_class=JSONResponse)
# async def list_machines():
#     conn = await asyncpg.connect(DATABASE_URL)
#     try:
#         rows = await conn.fetch("SELECT id, name, description, created_at FROM machine ORDER BY id")
#         data = [dict(r) for r in rows]
#         return JSONResponse(content=data)
#     finally:
#         await conn.close()
@router.get("/machines")
async def list_machines():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        rows = await conn.fetch("SELECT id, name, description, created_at FROM machine ORDER BY id")
        data = [dict(r) for r in rows]
        # Ensure datetime objects are serialized properly
        return jsonable_encoder(data)
    finally:
        await conn.close()

@router.post("/simulations", status_code=201)
async def create_simulation(payload: dict):
    # Strict fields: name, machine_id
    name = payload.get("name")
    mid = payload.get("machine_id")
    if not name or not mid:
        raise HTTPException(400, "name and machine_id required")
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        row = await conn.fetchrow("""
            INSERT INTO simulation(name, machine_id, status)
            VALUES($1,$2,'pending') RETURNING id, name, machine_id, status, created_at, updated_at
        """, name, mid)
        return dict(row)
    finally:
        await conn.close()

@router.get("/simulations")
async def list_simulations(status: Optional[str] = Query(None), order_by: Optional[str] = Query("created_at")):
    if order_by not in ("name","created_at","updated_at"):
        raise HTTPException(400,"invalid order_by")
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        if status:
            rows = await conn.fetch(f"SELECT * FROM simulation WHERE status=$1 ORDER BY {order_by}", status)
        else:
            rows = await conn.fetch(f"SELECT * FROM simulation ORDER BY {order_by}")
        return [dict(r) for r in rows]
    finally:
        await conn.close()

@router.get("/simulations/{simulation_id}")
async def simulation_detail(simulation_id: int):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        sim = await conn.fetchrow("SELECT * FROM simulation WHERE id=$1", simulation_id)
        if not sim:
            raise HTTPException(404,"not found")
        cps = await conn.fetch("SELECT seconds, loss FROM convergence_point WHERE simulation_id=$1 ORDER BY seconds", simulation_id)
        d = dict(sim)
        d["convergence"] = [dict(x) for x in cps]
        return d
    finally:
        await conn.close()

# SSE endpoint for live convergence streaming
import asyncio
async def event_stream(simulation_id: int):
    # This is a simple polling SSE: fetch new rows repeatedly and yield events
    last_seconds = -1
    while True:
        conn = await asyncpg.connect(DATABASE_URL)
        try:
            rows = await conn.fetch(
                "SELECT seconds, loss FROM convergence_point WHERE simulation_id=$1 AND seconds > $2 ORDER BY seconds",
                simulation_id, last_seconds
            )
            for r in rows:
                last_seconds = r["seconds"]
                payload = json.dumps({"seconds": r["seconds"], "loss": float(r["loss"])})
                yield f"data: {payload}\n\n"
            # stop streaming when simulation status is finished
            st = await conn.fetchval("SELECT status FROM simulation WHERE id=$1", simulation_id)
            if st == 'finished' and not rows:
                # push a final event then break
                yield f"event: finished\ndata: {{}}\n\n"
                break
        finally:
            await conn.close()
        await asyncio.sleep(1.0)

@router.get("/simulations/{simulation_id}/stream")
async def stream_convergence(simulation_id: int):
    return StreamingResponse(event_stream(simulation_id), media_type="text/event-stream")
