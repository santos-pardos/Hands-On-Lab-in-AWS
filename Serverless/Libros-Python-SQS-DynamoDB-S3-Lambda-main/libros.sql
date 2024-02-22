CREATE EXTERNAL TABLE IF NOT EXISTS libros (
  editorial STRING,
  anio_publicacion INT,
  genero STRING,
  titulo STRING,
  id STRING,
  autor STRING
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION 's3://project01-libros-raw-2024/';

-- SELECT * FROM libros;
