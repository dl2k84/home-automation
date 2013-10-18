DROP TABLE IF EXISTS REGISTERED_DEVICES
GO

CREATE TABLE REGISTERED_DEVICES(
    Id INTEGER NOT NULL
  , Name NVARCHAR(255) NOT NULL
  , Value NVARCHAR(255) NOT NULL
  , PRIMARY KEY(Id)
)
GO
