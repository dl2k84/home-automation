DROP TABLE IF EXISTS REFERENCE_LIGHTING_CODES
GO

CREATE TABLE REFERENCE_LIGHTING_CODES(
    StateId INT NOT NULL
  , Code BLOB NOT NULL
  , FormatId INT NOT NULL
  , MakerName NVARCHAR(255) NOT NULL
  , PRIMARY KEY(StateId, FormatId)
  , FOREIGN KEY(StateId) REFERENCES REFERENCE_LIGHTING(StateId)
  , FOREIGN KEY(FormatId) REFERENCES REFERENCE_MAKER_FORMAT(FormatId)
)
GO

/*
 * Insert byte code for NEC lights.
 * If you maker differs, then you will have to discover and test it for yourself.
 * Reference: https://gist.github.com/dl2k84/6081780
 */
INSERT INTO REFERENCE_LIGHTING_CODES(StateId, Code, FormatId, MakerName)
VALUES(0, '61022000826d1ae5', 2, 'nec')
  , (1, '61022000826d1ae5', 2, 'nec')
  , (2, '61022000826d1ae5', 2, 'nec')
  , (3, '61022000826d1ae5', 2, 'nec')
GO
