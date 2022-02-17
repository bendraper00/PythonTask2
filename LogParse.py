from pymavlink import DFReader
import matplotlib.pyplot as plt


if __name__ == "__main__":
    time = []
    roll = []
    pitch = []
    log = DFReader.DFReader_binary("data.bin")
    while True:
        m = log.recv_msg()
        if m is None:
            break
        if m.get_type() == "ATT": #Field names are TimeUS, Roll, Pitch
            time.append(m.TimeUS)
            roll.append(m.Roll)
            pitch.append(m.Pitch)

    x1 = time
    y1 = roll
    y2 = pitch
    plt.plot(x1, y1, label = "roll")
    plt.plot(x1, y2, label = "pitch")
    plt.xlabel('Time (uS)')
    plt.ylabel('Degrees (deg)')
    plt.title("Pitch and Roll over Time")
    plt.legend()
    plt.show()



        


