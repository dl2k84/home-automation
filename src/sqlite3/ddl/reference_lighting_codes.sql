DROP TABLE IF EXISTS REFERENCE_LIGHTING_CODES
GO

CREATE TABLE REFERENCE_LIGHTING_CODES(
    StateId INT NOT NULL
  , Code BLOB NOT NULL
  , PRIMARY KEY(StateId)
  , FOREIGN KEY(StateId) REFERENCES REFERENCE_LIGHTING(StateId)
)
GO

/*
 * Insert byte code for NEC lights.
 * If you maker differs, then you will have to discover and test it for yourself.
 * Reference: https://gist.github.com/dl2k84/6081780
 */
INSERT INTO REFERENCE_LIGHTING_CODES(StateId, Code)
VALUES(0, '61022000826d1ae5') 
  , (1, '61022000826d1ae5')
  , (2, '61022000826d1ae5')
  , (3, '61022000826d1ae5')
GO
