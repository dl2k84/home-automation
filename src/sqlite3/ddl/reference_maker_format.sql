DROP TABLE IF EXISTS REFERENCE_MAKER_FORMAT
GO

CREATE TABLE REFERENCE_MAKER_FORMAT(
    FormatId INT NOT NULL
  , Name NVARCHAR(255) NOT NULL
  , PRIMARY KEY(FormatId)
)
GO

/*
 * 1 = AEHA(Association for Electric Home Appliances)
 * 2 = NEC
 * 3 = Sony
 * 4 = Mitsubishi
 * 5 = Daikin-1
 * 6 = Daikin-2
 */
INSERT INTO REFERENCE_MAKER_FORMAT(FormatId, Name)
VALUES(1, "aeha")
  , (2, "nec")
  , (3, "sony")
  , (4, "mitsubishi")
  , (5, "daikin1")
  , (6, "daikin2")
GO
