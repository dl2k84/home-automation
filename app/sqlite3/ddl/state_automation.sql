DROP TABLE IF EXISTS STATE_AUTOMATION
GO

CREATE TABLE STATE_AUTOMATION(
    Id INTEGER NOT NULL
  , Name NVARCHAR(255) NOT NULL
  , Current_State INT NOT NULL
  , PRIMARY KEY(Id)
)
GO

INSERT INTO STATE_AUTOMATION(Name, Current_State)
VALUES('lighting', 0)
  , ('aircon_mode', 0)
  , ('aircon_temperature', 24)
  , ('aircon_wind_amount', 0)
  , ('aircon_wind_direction', 0)
  , ('aircon_timer_state', 0)
  , ('aircon_timer_hr', 0)
GO
