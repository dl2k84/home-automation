DROP TABLE IF EXISTS REFERENCE_LIGHTING
GO

CREATE TABLE REFERENCE_LIGHTING(
    StateId INT NOT NULL
  , Value NVARCHAR(255) NOT NULL
  , PRIMARY KEY(StateId)
)
GO

INSERT INTO REFERENCE_LIGHTING(StateId, Value)
VALUES(0, 'off')
  , (1, 'dim')
  , (2, 'on')
  , (3, 'bright')
GO

