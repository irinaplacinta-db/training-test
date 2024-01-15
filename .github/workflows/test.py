dbutils.fs.ls("abfss://external-location@testucirina.dfs.core.windows.net/shared/tables")
dbutils.fs.ls(get_uc_mount_target('/mnt/shared-tables', normalize=True) + "")


Hello dbfs:/mnt/shared-tables
