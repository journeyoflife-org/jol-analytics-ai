#!/usr/bin/env bash
# Export data lineage documentation from dbt models.
#
# Usage:
#   bash scripts/export-lineage.sh

set -euo pipefail

echo "=== Data Lineage Export ==="
echo ""

# Check for dbt project
if [ ! -d "src/jol_analytics_ai/dbt" ]; then
    echo "ERROR: dbt directory not found"
    exit 1
fi

echo "Scanning dbt models..."
find src/jol_analytics_ai/dbt/models -name "*.sql" -o -name "*.yml" 2>/dev/null | while read -r f; do
    echo "  - $f"
done

echo ""
echo "Scanning dbt sources..."
find src/jol_analytics_ai/dbt/sources -name "*.yml" 2>/dev/null | while read -r f; do
    echo "  - $f"
done

echo ""
echo "Scanning dbt exposures..."
find src/jol_analytics_ai/dbt/exposures -name "*.yml" 2>/dev/null | while read -r f; do
    echo "  - $f"
done

echo ""
echo "Lineage export complete."
echo "For full lineage, run: dbt docs generate"
