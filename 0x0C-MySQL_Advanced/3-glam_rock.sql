-- script that lists all bands with Glam rock as their main style
SELECT
  band_name,
  iFNULL(split, 2022) - formed AS lifespan
from
  metal_bands
where
  style LIKE "%Glam rock%"
ORDER BY
  lifespan DESC;