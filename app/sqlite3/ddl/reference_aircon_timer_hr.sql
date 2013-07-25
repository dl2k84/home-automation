DROP TABLE IF EXISTS REFERENCE_AIRCON_TIMER_HR
GO

CREATE TABLE REFERENCE_AIRCON_TIMER_HR(
    StateId INT NOT NULL
  , Value NVARCHAR(255) NOT NULL
  , PRIMARY KEY(StateId)
)
GO

INSERT INTO REFERENCE_AIRCON_TIMER_HR(StateId, Value)
VALUES(1, '1 hour')
  , (2, '2 hours')
  , (3, '3 hours')
  , (4, '4 hours')
  , (5, '5 hours')
  , (6, '6 hours')
  , (7, '7 hours')
  , (8, '8 hours')
  , (9, '9 hours')
  , (10, '10 hours')
  , (11, '11 hours')
  , (12, '12 hours')
GO
