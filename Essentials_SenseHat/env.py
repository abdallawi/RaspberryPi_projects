from sense_hat import SenseHat
sense = SenseHat()
while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    if t > 18.3 and t < 26.7:
        bg = [0, 100, 0]
    else:
        bg = [100, 0, 0]

    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t,p,h)
    msg_temperature = f"Temperature = {t}"
    msg_pressure = f"Pressure = {p}"
    msg_humidity = f"Humidity = {h}"
    sense.show_message(msg_temperature, scroll_speed=0.08, text_colour = bg)
    sense.show_message(msg_pressure, scroll_speed=0.08)
    sense.show_message(msg_humidity, scroll_speed=0.08)
