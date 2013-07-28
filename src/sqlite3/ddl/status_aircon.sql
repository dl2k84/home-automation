DROP TABLE IF EXISTS STATUS_AIRCON
GO

CREATE TABLE STATUS_AIRCON(
    CODE BLOB NOT NULL
  , PRIMARY KEY(CODE)
)
GO

/*
 * Insert a mask value as default. These masks need changing else
 * db.getAirconStatus won't work until a setting is applied
 * via db.setAircon
 */
INSERT INTO STATUS_AIRCON VALUES('610140980220e004000000060220e004003ghh80af000006600000800016ii')
GO
