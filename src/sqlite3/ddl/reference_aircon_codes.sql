DROP TABLE IF EXISTS REFERENCE_AIRCON_CODES
GO

CREATE TABLE REFERENCE_AIRCON_CODES(
    StateId INT NOT NULL
  , Code BLOB NOT NULL
  , FormatId INT NOT NULL
  , MakerName NVARCHAR(255) NOT NULL
  , PRIMARY KEY(StateId, FormatId)
  , FOREIGN KEY(StateId) REFERENCES REFERENCE_AIRCON_MODE(StateId)
  , FOREIGN KEY(FormatId) REFERENCES REFERENCE_MAKER_FORMAT(FormatId)
)
GO

/*
 * Insert base byte code for aircon
 * These codes are for Panasonic make.
 * If you maker/format differs, then you will have to discover and test it for yourself.
 * Reference: https://gist.github.com/dl2k84/6081780
 *
 * N.B., these base codes contain input  masks in them that needs to be
 * processed and replaced by the business logic layer
 * otherwise in its current state they are invalid hex
 * representations of a byte stream.
 *
 * Mask spec:
 * g: on/off mask
 * hh: temperature control code 1
 * ii: temperature control code 2 
 */
INSERT INTO REFERENCE_AIRCON_CODES(StateId, Code, FormatId, MakerName)
VALUES(1, '610140980220e004000000060220e004003ghh80af000006600000800016ii', 1, 'panasonic')
  , (2, '', 1, 'panasonic')
  , (3, '', 1, 'panasonic')
GO
