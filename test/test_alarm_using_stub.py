from unittest.mock import Mock
from src.alarm import Alarm
from src.sensor import Sensor


def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert alarm.is_alarm_on == False


def test_alarm_is_on_at_lower_threshold():
    sensor = Mock(Sensor)
    sensor.sample_pressure.return_value = 17.0
    alarm = Alarm(sensor=sensor)
    alarm.check()
    assert alarm.is_alarm_on == True


def test_alarm_is_on_at_higher_threshold():
    sensor = Mock(Sensor)
    sensor.sample_pressure.return_value = 21.0
    alarm = Alarm(sensor=sensor)
    alarm.check()
    assert alarm.is_alarm_on == True
