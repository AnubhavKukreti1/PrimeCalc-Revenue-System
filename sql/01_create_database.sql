
-- =====================================================
-- PROJECT: RevenueX
-- MODULE: Database Initialization
-- DATABASE: revenuex
-- DESCRIPTION: Create analytical database schemas
-- =====================================================

-- Create schemas
CREATE SCHEMA IF NOT EXISTS raw;

CREATE SCHEMA IF NOT EXISTS staging;

CREATE SCHEMA IF NOT EXISTS analytics;

-- Verify schemas
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name IN (
    'raw',
    'staging',
    'analytics'
)
ORDER BY schema_name;
