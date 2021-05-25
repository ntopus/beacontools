"""All low level structures used for parsing minew packets."""
from construct import Float16b, Int8ub

from ..const import (MINEW_MANUFACTURER_UUID, MINEW_S1_BATTERY_LEVEL,
                     MINEW_S1_HUMIDITY, MINEW_S1_TEMPERATURE)

# pylint: disable=invalid-name

MinewS1Frame = Struct(
    "battery_level" / Int8ub,
    "temperature" / Float16b,
    "humidity" / Float16b,
)
