DROP TABLE IF EXISTS REFERENCE_AIRCON_MODE
GO

CREATE TABLE REFERENCE_AIRCON_MODE(
    StateId INT NOT NULL
  , Value NVARCHAR(255) NOT NULL
  , PRIMARY KEY(StateId)
)
GO

INSERT INTO REFERENCE_AIRCON_MODE(StateId, Value)
VALUES(0, 'aircon')
  , (1, 'dehumidifier')
  , (2, 'heater')
GO