import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.components import canbus
from esphome.const import CONF_ID, CONF_RX_PIN, CONF_TX_PIN
from esphome.components.canbus import CanbusComponent

esp32_can_ns = cg.esphome_ns.namespace("esp32_can")
esp32_can = esp32_can_ns.class_("ESP32Can", CanbusComponent)

CONFIG_SCHEMA = canbus.CANBUS_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(esp32_can),
        cv.Required(CONF_RX_PIN): pins.gpio_output_pin_schema,
        cv.Required(CONF_TX_PIN): pins.gpio_output_pin_schema,
    }
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield canbus.register_canbus(var, config)

    cg.add_library("sandeepmistry/CAN", "~0.3.1")
