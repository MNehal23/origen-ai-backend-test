-- Create machine table
CREATE TABLE IF NOT EXISTS machine (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  description TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Safely create enum type for simulation status
DO $$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'sim_status') THEN
      CREATE TYPE sim_status AS ENUM ('pending','running','finished');
   END IF;
END$$;

-- Create simulation table
CREATE TABLE IF NOT EXISTS simulation (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  machine_id INTEGER NOT NULL REFERENCES machine(id) ON DELETE CASCADE,
  status sim_status NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Create convergence points table
CREATE TABLE IF NOT EXISTS convergence_point (
  id SERIAL PRIMARY KEY,
  simulation_id INTEGER NOT NULL REFERENCES simulation(id) ON DELETE CASCADE,
  seconds INTEGER NOT NULL,
  loss DOUBLE PRECISION NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
