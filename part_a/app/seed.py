# part_a/app/seed.py
# Optional helper to create a sample simulation and insert convergence points (for manual/manual demo)
import asyncio, asyncpg, random, time
from app.db.database import DATABASE_URL

async def create_demo():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        sim = await conn.fetchrow("INSERT INTO simulation(name, machine_id, status) VALUES($1,$2,'running') RETURNING id", "demo-sim", 1)
        sim_id = sim['id']
        # stream some convergence points
        for s in range(10, 200, 10):
            await conn.execute("INSERT INTO convergence_point(simulation_id, seconds, loss) VALUES($1,$2,$3)",
                               sim_id, s, round(random.uniform(0.4,0.8) - (s/1000.0),4))
            await asyncio.sleep(0.05)  # fast seed, not for production
        # finish
        await conn.execute("UPDATE simulation SET status='finished', updated_at=now() WHERE id=$1", sim_id)
        print("Demo created", sim_id)
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(create_demo())
