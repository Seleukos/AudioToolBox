"""
multi.py, uses the sounddevice library to play multiple audio files to multiple output devices at the same time
Written by Devon Bray (dev@esologic.com)
"""

import sounddevice
import soundfile
import threading
import os

import sounddevice as sd


DATA_TYPE = "float32"


def load_sound_file_into_memory(path):
    """
    Get the in-memory version of a given path to a wav file
    :param path: wav file to be loaded
    :return: audio_data, a 2D numpy array
    """

    audio_data, _ = soundfile.read(path, dtype=DATA_TYPE)
    return audio_data


def get_device_number_if_usb_soundcard(index_info):
    """
    Given a device dict, return True if the device is one of our USB sound cards and False if otherwise
    :param index_info: a device info dict from PyAudio.
    :return: True if usb sound card, False if otherwise
    """

    index, info = index_info

    if "USB Audio Device" in info["name"]:
        return index
    return False

def get_device_number_if_audio_outputdevice_all(index_info):
    list_audiodevices = sd.query_devices()

    print(list_audiodevices)


    index, info = index_info

    if "Output" in info["name"]:
        return index
    # list -> transform given input (tuple) into a list
    # filter -> sorts the given tuple or lsit
    # map -> (function which takes everey item of the list, list)
    # get_device_number_if_usb_soundcard _> thats the function which is used for every item of index_info)
    # index_info
    # sounddevice.query_devices()
    usb_sound_card_indices = list(filter(lambda x: x is not False,
                                         map(get_device_number_if_usb_soundcard,
                                             [index_info for index_info in
                                              enumerate(sounddevice.query_devices())])))

    print("Discovered the following audio output devices", usb_sound_card_indices)
    return False







def get_device_number_if_audio_inputdevice_all(index_info):
    pass


def get_device_number_if_audio_outputdevice_usb(index_info):
    pass

def get_device_number_if_audio_inputdevice_usb(index_info):
    pass

def get_device_number_if_audio_outputdevice_phone(index_info):
    pass

def get_device_number_if_audio_inputdevice_phone(index_info):
    pass



def play_wav_on_index(audio_data, stream_object):
    """
    Play an audio file given as the result of `load_sound_file_into_memory`
    :param audio_data: A two-dimensional NumPy array
    :param stream_object: a sounddevice.OutputStream object that will immediately start playing any data written to it.
    :return: None, returns when the data has all been consumed
    """

    stream_object.write(audio_data)


def create_running_output_stream(index):
    """
    Create an sounddevice.OutputStream that writes to the device specified by index that is ready to be written to.
    You can immediately call `write` on this object with data and it will play on the device.
    :param index: the device index of the audio device to write to
    :return: a started sounddevice.OutputStream object ready to be written to
    """

    output = sounddevice.OutputStream(
        device=index,
        dtype=DATA_TYPE
    )
    output.start()
    return output


def playback_audiofile_from_usbdevice(sound_file_paths):

    def good_filepath(path):
        """
        Macro for returning false if the file is not a non-hidden wav file
        :param path: path to the file
        :return: true if a non-hidden wav, false if not a wav or hidden
        """
        return str(path).endswith(".wav") and (not str(path).startswith("."))

    # The method getcwd() returns current working directory of a process.

    # Follwoing part isues, when no filepath_of_wavfile
    cwd = os.getcwd()
    #filepath_of_wavfile = [os.path.join(cwd, path) for path in sorted(filter(lambda path: good_filepath(path), os.listdir(cwd)))]

    '''
    sound_file_paths = [
        os.path.join(filepath_of_wavfile, path) for path in sorted(filter(lambda path: good_filepath(path),
                                                                          os.listdir(filepath_of_wavfile)))
    ]
    '''

    # List with all absolute pathes of the found wav.-files:
    #sound_file_paths = ['C:\\Users\\t02meyer\\PycharmProjects\\AUTOBO\\directory_audio_file\\delme_rec_unlimited_903f28uh.wav']
    #sound_file_paths = ['C:\\Users\\t02meyer\\PycharmProjects\\AUTOBO\\directory_audio_file\\1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav']
    sound_file_paths= ['C:\\Users\\Tobi_SurfacePro\\PycharmProjects\\AudioToolBox\\directory_audio_file\\Jungle Windows Start.wav']

    print("Discovered the following .wav files:", sound_file_paths)

    files = [load_sound_file_into_memory(path) for path in sound_file_paths]

    print("Files loaded into memory, Looking for USB devices.")

    # list -> transform given input (tuple) into a list
    # filter -> sorts the given tuple or lsit
    # map -> (function which takes everey item of the list, list)
    # get_device_number_if_usb_soundcard _> thats the function which is used for every item of index_info)
    # index_info
    #sounddevice.query_devices()
    #usb_sound_card_indices = list(filter(lambda x: x is not False,
    #                                     map(get_device_number_if_usb_soundcard,
    #                                         [index_info for index_info in enumerate(sounddevice.query_devices())])))

    #print("Discovered the following usb sound devices", usb_sound_card_indices)

    ### There must be a query, which asks for which index should be used for a playback!!!
    ### Afterwards there are created streams for every output

    usb_sound_card_indices = [3]
    #sd.default.device = 3

    streams = [create_running_output_stream(index) for index in usb_sound_card_indices]

    running = True

    if not len(streams) > 0:
        running = False
        print("No audio devices found, stopping")

    if not len(files) > 0:
        running = False
        print("No sound files found, stopping")

    while running:

        print("Playing files")

        threads = [threading.Thread(target=play_wav_on_index, args=[file_path, stream])
                   for file_path, stream in zip(files, streams)]

        try:

            for thread in threads:
                thread.start()

            for thread, device_index in zip(threads, usb_sound_card_indices):
                print("Waiting for device", device_index, "to finish")
                thread.join()
        # With a type on the keyboard all streams are interrupted!
        except KeyboardInterrupt:
            running = False
            print("Stopping stream")
            for stream in streams:
                stream.abort(ignore_errors=True)
                stream.close()
            print("Streams stopped")

    print("Bye.")

