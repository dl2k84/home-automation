DROP TABLE IF EXISTS REFERENCE_LIGHTING_CODES
GO

CREATE TABLE REFERENCE_LIGHTING_CODES(
    Code BLOB NOT NULL
  , PRIMARY KEY(Code)
)
GO

/*
 * Insert byte code for NEC lights.
 * If you maker differs, then you will have to discover and test it for yourself.
 * Reference: https://gist.github.com/dl2k84/6081780
 */
INSERT INTO REFERENCE_LIGHTING_CODES(Code)
VALUES('61022000826d1ae5') 
GO
