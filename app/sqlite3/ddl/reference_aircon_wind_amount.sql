DROP TABLE IF EXISTS REFERENCE_AIRCON_WIND_AMOUNT
GO

CREATE TABLE REFERENCE_AIRCON_WIND_AMOUNT(
    StateId INT NOT NULL
  , Value NVARCHAR(255) NOT NULL
  , PRIMARY KEY(StateId)
)
GO

INSERT INTO REFERENCE_AIRCON_WIND_AMOUNT(StateId, Value)
VALUES(0, 'level1')
  , (1, 'level2')
  , (2, 'level3')
  , (3, 'level4')
  , (4, 'auto')
  , (5, 'quiet')
GO
