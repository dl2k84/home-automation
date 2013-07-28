DROP TABLE IF EXISTS REFERENCE_AIRCON_CODE_TYPE
GO

CREATE TABLE REFERENCE_AIRCON_CODE_TYPE(
    Id INTEGER NOT NULL
  , Code BLOB NOT NULL
  , CodeValue NVARCHAR(255) NOT NULL
  , TypeName NVARCHAR(255) NOT NULL
  , MakerName NVARCHAR(255) NOT NULL
  , PRIMARY KEY(Id)
  , FOREIGN KEY(MakerName) REFERENCES REFERENCE_AIRCON_CODES(MakerName)
)
GO

INSERT INTO REFERENCE_AIRCON_CODE_TYPE(Code, CodeValue, TypeName, MakerName)
VALUES('0', '0', 'off', 'panasonic')
  , ('1', '1', 'on', 'panasonic')
  , ('28', '20', 'temperature-min-1', 'panasonic')
  , ('8a', '20', 'temperature-min-2', 'panasonic')
  , ('38', '28', 'temperature-max-1', 'panasonic')
  , ('9a', '28', 'temperature-max-2', 'panasonic')
GO
