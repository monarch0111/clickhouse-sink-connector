"""Default configuration for the ClickHouse Sink Connector."""

default_config = {
    "name": "my_connector",
    "database.hostname": "mysql-master",
    "database.port": "3306",
    "database.user": "root",
    "database.password": "root",
    "database.server.name": "ER54",
    "database.include.list": "test",
    "clickhouse.server.url": "clickhouse",
    "clickhouse.server.user": "root",
    "clickhouse.server.password": "root",
    "clickhouse.server.port": "8123",
    "clickhouse.server.database": "test",
    "database.allowPublicKeyRetrieval": "true",
    "snapshot.mode": "initial",
    "offset.flush.interval.ms": "5000",
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "offset.storage": "io.debezium.storage.jdbc.offset.JdbcOffsetBackingStore",
    "offset.storage.jdbc.offset.table.name": "altinity_sink_connector.replica_source_info",
    "offset.storage.jdbc.url": "jdbc:clickhouse://clickhouse:8123/altinity_sink_connector",
    "offset.storage.jdbc.user": "root",
    "offset.storage.jdbc.password": "root",
    "offset.storage.jdbc.offset.table.ddl": """CREATE TABLE if not exists %s
(
    `id` String,
    `offset_key` String,
    `offset_val` String,
    `record_insert_ts` DateTime,
    `record_insert_seq` UInt64,
    `_version` UInt64 MATERIALIZED toUnixTimestamp64Nano(now64(9))
)
ENGINE = ReplacingMergeTree(_version)
ORDER BY id
SETTINGS index_granularity = 8198""",
    "offset.storage.jdbc.offset.table.delete": "delete from %s where 1=1",
    "schema.history.internal": "io.debezium.storage.jdbc.history.JdbcSchemaHistory",
    "schema.history.internal.jdbc.url": "jdbc:clickhouse://clickhouse:8123/altinity_sink_connector",
    "schema.history.internal.jdbc.user": "root",
    "schema.history.internal.jdbc.password": "root",
    "schema.history.internal.jdbc.schema.history.table.ddl": """CREATE TABLE if not exists %s
(`id` VARCHAR(36) NOT NULL, `history_data` VARCHAR(65000), `history_data_seq` INTEGER, `record_insert_ts` TIMESTAMP NOT NULL, `record_insert_seq` INTEGER NOT NULL) ENGINE=ReplacingMergeTree(record_insert_seq) order by id""",
    "schema.history.internal.jdbc.schema.history.table.name": "altinity_sink_connector.replicate_schema_history",
    "replacingmergetree.delete.column": "_sign",
    "enable.snapshot.ddl": "true",
    "database.connectionTimeZone": "UTC",
    "database.serverTimezone": "UTC",
    "clickhouse.datetime.timezone": "UTC",
    "auto.create.tables": "true",
}
