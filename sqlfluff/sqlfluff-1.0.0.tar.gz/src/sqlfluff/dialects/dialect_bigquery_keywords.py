"""A list of all BigQuery SQL key words."""

# https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#reserved_keywords
bigquery_reserved_keywords = """ALL
AND
ANY
ARRAY
AS
ASC
ASSERT_ROWS_MODIFIED
AT
BETWEEN
BY
CASE
CAST
COLLATE
CONTAINS
CREATE
CROSS
CUBE
CURRENT
DEFAULT
DEFINE
DESC
DISTINCT
ELSE
END
ENUM
ESCAPE
EXCEPT
EXCLUDE
EXISTS
FALSE
FETCH
FOLLOWING
FOR
FROM
FULL
GROUP
GROUPING
GROUPS
HASH
HAVING
IF
IGNORE
IN
INCLUDE
INNER
INTERSECT
INTERVAL
INTO
IS
JOIN
LATERAL
LEFT
LIKE
LIMIT
LOOKUP
MERGE
NEW
NO
NOT
NULL
NULLS
OF
ON
OR
ORDER
OUTER
OVER
PARTITION
PIVOT
PRECEDING
PROTO
RANGE
RECURSIVE
RESPECT
RIGHT
ROLLUP
ROWS
SELECT
SET
SOME
STRUCT
TABLESAMPLE
THEN
TO
TREAT
TRUE
UNBOUNDED
UNION
UNNEST
UNPIVOT
USING
WHEN
WHERE
WINDOW
WITH
WITHIN"""

# Note BigQuery doesn't have a list of Unreserved Keywords
# so these are just ones we need to allow parsing to work
bigquery_unreserved_keywords = """ACCOUNT
ADD
ADMIN
AFTER
ALTER
APPLY
ASSERT
AUTO_INCREMENT
BEGIN
BERNOULLI
BINARY
BINDING
CACHE
CALL
CASCADE
CHAIN
CHARACTER
CHECK
CLUSTER
COLUMN
COLUMNS
COMMENT
COMMIT
CONCURRENTLY
CONNECT
CONNECTION
CONSTRAINT
COPY
CURRENT_USER
CYCLE
DATA
DATABASE
DATE
DATETIME
DECLARE
DELETE
DESCRIBE
DETERMINISTIC
DO
DOMAIN
DOUBLE
DROP
EXECUTE
EXECUTION
EXPLAIN
EXPORT
EXTENSION
EXTERNAL
FILE
FILTER
FIRST
FOREIGN
FORMAT
FUNCTION
FUTURE
GRANT
GRANTED
GRANTS
HOUR
ILIKE
IMPORTED
IN
INCREMENT
INDEX
INOUT
INSERT
INTEGRATION
KEY
LANGUAGE
LARGE
LAST
MANAGE
MASKING
MATCHED
MATERIALIZED
MAXVALUE
MESSAGE
MINUS
MINVALUE
ML
MODEL
MODIFY
MONITOR
NAME
NAN
NFC
NFKC
NFD
NFKD
NOCACHE
NOCYCLE
NOORDER
OBJECT
OFFSET
OPERATE
OPTION
OPTIONS
ORDINAL
OUT
OVERLAPS
OVERWRITE
OWNERSHIP
PERCENT
PIPE
POLICY
PRECISION
PRIMARY
PRIOR
PRIVILEGES
PROCEDURE
PUBLIC
QUALIFY
QUARTER
RAISE
READ
REFERENCE_USAGE
REFERENCES
RENAME
REPEATABLE
REPLACE
RESOURCE
RESTRICT
RETURN
RETURNS
REVOKE
RLIKE
ROLE
ROLLBACK
ROW
ROUTINE
SAFE
SCHEMA
SCHEMAS
SECOND
SEPARATOR
SERVER
SEQUENCE
SESSION_USER
SHARE
SOURCE
STAGE
START
STREAM
SYSTEM
SYSTEM_TIME
TABLE
TABLESPACE
TARGET
TASK
TEMP
TEMPORARY
TIME
TIMESTAMP
TRANSACTION
TRANSIENT
TRIGGER
TRUNCATE
TYPE
UNIQUE
UNSIGNED
UPDATE
USAGE
USE
USE_ANY_ROLE
USER
VALUE
VALUES
VARYING
VERSION
VIEW
WAREHOUSE
WITHOUT
WORK
WRAPPER
WRITE
ZONE"""
